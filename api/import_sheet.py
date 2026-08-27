from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Property, Agreement, Payment

from openpyxl import load_workbook

class ImportUsers(APIView):
    def post(self, request):
        file = request.FILES.get("file")

        spreadsheet = load_workbook(file)

        sheet = spreadsheet["Usuarios"]

        created = 0
        ignored = 0

        for column in sheet.iter_rows(min_row=2, values_only=True):
            username = column[0]
            first_name = column[1]
            last_name = column[2]
            email = column[3]
            telephone = column[4]
            user_type = column[5]
            is_active = column[6]
            password = column[7]

            if User.objects.filter(username=username).exists():
                ignored += 1
                continue

            user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                telephone=telephone,
                user_type=user_type,
                is_active=is_active,
                password=password
            )

        return Response({"message": "Planilha lida com sucesso!"})