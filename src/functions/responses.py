def ResponseMaker(status, message, contentName = False, content = False):
  response = {}
  response["status"] = status
  response["message"] = message

  if(contentName and content):
    response[contentName] = content
  
  return response