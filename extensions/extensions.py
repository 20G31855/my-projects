Filename = input("Filename:").lower().strip()
if Filename.endswith(".gif"):
    print("image/gif")
elif Filename.endswith(".jpg") or Filename.endswith(".jpeg"):
    print("image/jpeg")
elif Filename.endswith(".png"):
    print("image/png")
elif Filename.endswith(".pdf"):
    print("application/pdf")
elif Filename.endswith(".txt"):
    print("text/plain")
elif Filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")










