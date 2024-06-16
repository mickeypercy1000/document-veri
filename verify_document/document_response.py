def doc_response(image, document):
    return {
        "code": 200,
        "success": True,
        "verificationSuccess": True,
        "message": "verification successful",
        "verificationDetails": {
            "idNumber": "28409244410",
            "idType": "IDENTITY_CARD",
            "candidateDetails": {
                "firstName": document["names"],
                "middleName": "",
                "lastName": document["surname"],
                "fullname": "CHIZOTA EBUKA, VICTOR",
                "fullname": document["names"] + " " + document["surname"],
                "address": "Not Available",
                "phoneNumber": "Not Available",
                "dateOfbirth": document["date_of_birth"],
                "gender": document["sex"],
                "residentialAddress": "",
                "nationality": document["country"],
                "nationalIdNo": "",
                "fathersName": "",
                "mothersName": "",
                "placeOfBirth": "",
                "age": "",
                "picture": None
            },
            "idDetails": {
                "registrationDate": "",
                "placeOfIssue": "",
                "issueDate": "",
                "expiryDate": document["expiration_date"],
                "processingCenter": "",
                "pin": "",
                "classOfLicence": "",
                "certificateDate": "",
                "certificateOfCompetence": "",
                "cardSerial": "",
                "fssNo": "",
                "pollingStation": "",
                "age": "",
                "dateOfFirstLicence": ""
            },
            "jobDetails": {
                "referenceId": "db8be822-6ba9-4b57-a537-c4fe15c5a929",
                "timestamp": "2024-06-12T08:28:33.991263Z"
            }
        }
    }