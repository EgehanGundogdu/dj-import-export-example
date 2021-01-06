from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from example.resources import DriverResource

class Export(View):
    template_name = "example/export.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        file_type = request.POST.get("file_type")
        dataset = DriverResource().export()
        if file_type == "csv":
            response = HttpResponse(dataset.csv, content_type="text/csv")
            response["Content-Disposition"] = 'attachment; filename="driver.csv"'
            return response
        elif file_type == "json":
            response = HttpResponse(dataset.json, content_type="text/json")
            response["Content-Disposition"] = 'attachment; filename="driver.json"'
        elif file_type == "excel":
            response = HttpResponse(
                dataset.xlsx,
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            response["Content-Disposition"] = 'attachment; filename="driver.xlsx"'
        else:
            response = JsonResponse({"message": "unsupported file type"}, status=400)
        return response


from tablib import Dataset


class Import(View):
    template_name = "example/import.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        resource = DriverResource()
        new_drivers = request.FILES["import_file"]
        file_type = str(new_drivers).split(".")[-1]
        dataset = Dataset()
        imported_data = dataset.load(
            new_drivers.read().decode("utf-8"), format=file_type
        )
        result = resource.import_data(
            dataset, dry_run=True
        )
        if not result.has_errors():
            resource.import_data(dataset, dry_run=False)
        else:

            return HttpResponse('some errors on your file.')
        return render(request, self.template_name, {})
