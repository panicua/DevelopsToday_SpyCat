from rest_framework import viewsets, permissions
from rest_framework.response import Response

from Mission.models import Mission, Target
from Mission.serializers import MissionSerializer
from SpyCat.models import SpyCat


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        mission_data = request.data
        targets_data = request.data.get("targets", [])
        if not (1 <= len(targets_data) <= 3):
            return Response(
                {"error": "Mission must have between 1 and 3 targets"},
                status=400
            )

        mission = Mission.objects.create(
            **{k: v for k, v in mission_data.items() if k != 'targets'}
        )
        targets = [Target.objects.create(**target_data) for target_data in targets_data]
        mission.targets.set(targets)

        return Response({"message": "Mission created successfully"})

    def update(self, request, *args, **kwargs):
        mission = self.get_object()
        targets_data = request.data.get("targets", [])
        cat_id = request.data.get("cat")

        if cat_id:
            cat = SpyCat.objects.get(id=cat_id)
            if mission.cat:
                return Response(
                    {"error": "Mission already has a cat assigned"}, status=400
                )
            if cat.missions.filter(complete=False).exists():
                return Response(
                    {"error": "Cat is already assigned to another mission"},
                    status=400,
                )
            mission.cat = cat
            mission.save()

        for target_data in targets_data:
            target = Target.objects.get(id=target_data["id"])
            if mission not in target.missions.all():
                return Response(
                    {"error": "Target does not belong to this mission"},
                    status=400,
                )
            if (target.complete or mission.complete) and target_data.get("notes"):
                return Response(
                    {
                        "error": "Notes cannot be updated if either the "
                        "target or the mission is completed"
                    },
                    status=400,
                )
            target.notes = target_data.get("notes", target.notes)
            target.complete = target_data.get("complete", target.complete)
            target.save()

        if all(target.complete for target in mission.targets.all()):
            mission.complete = True
            mission.save()

        return Response({"message": "Mission updated successfully"})

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.cat:
            return Response(
                {"error": "Mission cannot be deleted if it is already assigned to a cat"},
                status=400,
            )
        mission.delete()
        return Response({"message": "Mission deleted successfully"})
