import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, inputDocument: func.DocumentList) -> str:
##if not inputDocument:
##logging.warning("ToDo item not not found")
    users_json = []

    for user in inputDocument:
        user_json = {
          ## "id": user['id'],
           ##"partitionkey": user['testpartitionkey'],
           "visit nr is: ": user['visitor']
        }
        users_json.append(user_json)

    if inputDocument:
        return func.HttpResponse(
            json.dumps(users_json),
            status_code=420,
            mimetype="application/json"            
        )
##return func.HttpResponse (f"Hello, {inputDocument.sort}. This HTTP triggered function executed successfully")
    else:
        return func.HttpResponse(
            "this trigger was executed sucessfully, please pass in a query in the requestbody",
            status_code=555
        )

 ##THIS IS WORKING