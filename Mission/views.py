from rest_framework import viewsets, permissions
from rest_framework.response import Response

from Mission.models import Mission, Target
from Mission.serializers import MissionSerializer, TargetSerializer
from SpyCat.models import SpyCat


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        cat_id = request.data["cat"]
        cat = SpyCat.objects.get(id=cat_id)
        mission_data = {"cat": cat, "complete": request.data["complete"]}
        mission = Mission.objects.create(**mission_data)
        targets_data = request.data["targets"]

        # Unique target name inside of mission check
        set_of_names = {target_data["name"] for target_data in targets_data}
        if len(set_of_names) != len(targets_data):
            return Response(
                {"error": "Target names must be unique"}, status=400
            )

        for target_data in targets_data:
            target = Target.objects.create(**target_data)
            mission.targets.add(target)

    def update(self, request, *args, **kwargs):
        mission = self.get_object()
        targets_data = request.data.get("targets", [])

        for target_data in targets_data:
            target = Target.objects.get(id=target_data["id"])
            print(target_data.get("notes"))
            if (target.complete or mission.complete) and target_data.get(
                "notes"
            ):
                return Response(
                    {
                        "error": "Notes cannot be updated if either the target or the mission is completed"
                    },
                    status=400,
                )
            target.notes = target_data.get("notes", target.notes)
            target.complete = target_data.get("complete", target.complete)
            target.save()

        mission.complete = request.data.get("complete", mission.complete)
        mission.save()

        return Response({"message": "Mission targets updated successfully"})

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.cat:
            return Response(
                {
                    "error": "Mission cannot be deleted if "
                    "it is already assigned to a cat"
                },
                status=400,
            )
        mission.delete()
        return Response({"message": "Mission deleted successfully"})


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, request, *args, **kwargs):
        target = self.get_object()
        mission = target.mission

        if target.complete or mission.complete:
            return Response(
                {
                    "error": "Notes cannot be updated if either the target or the mission is completed"
                },
                status=400,
            )

        target.notes = request.data.get("notes", target.notes)
        target.complete = request.data.get("complete", target.complete)
        target.save()

        return Response({"message": "Target updated successfully"})
