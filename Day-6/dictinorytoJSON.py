import json

data = {
    'api': '/v2/events',
    'userToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTY5ODA5OTM2NSwiaWF0IjoxNjk4MDEyOTY1LCJpc3MiOiJUUyIsImp0aSI6IjYxZTRlMmFhNTY5MTQ4NjdiMDZlZGZjZGU0MzFhZTk3Iiwic3ViIjoie1wiaElkXCI6XCJiYzAxNGNkYjE1NTQ0YzMyOGVmODc5Yjg1YThkZTYwNFwiLFwicElkXCI6XCJjMThkOWNjZWRiNWM0MDcxYmU3MDc0MmU2ZTY5YmRiZFwiLFwibmFtZVwiOlwiQW51cmFnXCIsXCJwaG9uZVwiOlwiNzI5MTk3MTc1M1wiLFwiaXBcIjpcIjI0MDI6ODEwMDoyNjc4Ojc1MWI6MWU5OmI0MDI6Mzk3Nzo1YTcwXCIsXCJjb3VudHJ5Q29kZVwiOlwiaW5cIixcImN1c3RvbWVyVHlwZVwiOlwibnVcIixcInR5cGVcIjpcInBob25lXCIsXCJpc0VtYWlsVmVyaWZpZWRcIjpmYWxzZSxcImlzUGhvbmVWZXJpZmllZFwiOnRydWUsXCJkZXZpY2VJZFwiOlwiM2IxYWFiLTcwNDJhZS01OTNlNDAtMjU2MmY0XCIsXCJwcm9maWxlXCI6XCJBRFVMVFwiLFwidmVyc2lvblwiOlwidjJcIixcInN1YnNjcmlwdGlvbnNcIjp7XCJpblwiOntcIkhvdHN0YXJTdXBlclwiOntcInN0YXR1c1wiOlwiU1wiLFwiZXhwaXJ5XCI6XCIyMDIzLTEyLTExVDEwOjEwOjQzLjAwMFpcIixcInNob3dBZHNcIjpcIjFcIixcImNudFwiOlwiMVwifX19LFwiZW50XCI6XCJDclVCQ2dVS0F3b0JCUktyQVJJSFlXNWtjbTlwWkJJRGFXOXpFZ04zWldJU0NXRnVaSEp2YVdSMGRoSUdabWx5WlhSMkVnZGhjSEJzWlhSMkVnUnRkMlZpRWdkMGFYcGxiblIyRWdWM1pXSnZjeElHYW1sdmMzUmlFZ1J5YjJ0MUVnZHFhVzh0YkhsbUVncGphSEp2YldWallYTjBFZ1IwZG05ekVnUndZM1IyRWdOcWFXOGFBbk5rR2dKb1pCb0RabWhrSWdOelpISXFCbk4wWlhKbGJ5b0laRzlzWW5rMUxqRXFDbVJ2YkdKNVFYUnRiM05ZQVFvTkVnc0lBamdDUUFGUXVBaFlBUW9pQ2hvS0RoSUZOVFU0TXpZU0JUWTBNRFE1Q2dnaUJtWnBjbVYwZGhJRU9HUllBUXJJQVFvRkNnTUtBUUFTdmdFU0IyRnVaSEp2YVdRU0EybHZjeElEZDJWaUVnbGhibVJ5YjJsa2RIWVNCbVpwY21WMGRoSUhZWEJ3YkdWMGRoSUViWGRsWWhJSGRHbDZaVzUwZGhJRmQyVmliM01TQm1wcGIzTjBZaElFY205cmRSSUhhbWx2TFd4NVpoSUtZMmh5YjIxbFkyRnpkQklFZEhadmN4SUVjR04wZGhJRGFtbHZFZ1I0WW05NEVndHdiR0Y1YzNSaGRHbHZiaG9DYzJRYUFtaGtHZ05tYUdRaUEzTmtjaW9HYzNSbGNtVnZLZ2hrYjJ4aWVUVXVNU29LWkc5c1lubEJkRzF2YzFnQkVuMElBUkM0a2U3Q3hURWFSd29iVm1rdVNVNHVVM1Z3WlhJdVdXVmhjbXg1TGxCdmMzUndZV2xrRWd4SWIzUnpkR0Z5VTNWd1pYSWFDRlp2WkdGbWIyNWxJTGk1cVlYUU1DaTRrZTdDeFRFd0J6Z0JLQUV3QVRvbENpRkliM1J6ZEdGeVUzVndaWEl1UVdSelJuSmxaUzVKVGk1WlpXRnlMakV3T1RrUUFRPT1cIixcImlzc3VlZEF0XCI6MTY5ODAxMjk2NTg2MSxcIm1hdHVyaXR5TGV2ZWxcIjpcIkFcIixcImRwaWRcIjpcImMxOGQ5Y2NlZGI1YzQwNzFiZTcwNzQyZTZlNjliZGJkXCIsXCJzdFwiOjEsXCJkYXRhXCI6XCJDZ1FJQUJJQUNnUUlBRG9BQ2dRSUFESUFDaElJQUNJT2dBRVNpQUVCa0FHWXVLbUYwREFLQkFnQVFnQUtpZ0VJQUNxRkFRb0NDZ0FLR0FvQ0NBSVNCUW9EYUdsdUVnVUtBMlZ1WnhqSWd0R3BCZ28vQ2djSUFSVUFBQUJBRWdvS0EyVnVaeVdDM1lVOEVnb0tBM1JoYlNXbzNmWTdFZ29LQTJocGJpWHN0M2svRWdvS0EydGhiaVhOc0MwNkdNaUMwYWtHQ2hFS0FnZ0RFZ1VLQTJocGJoaklndEdwQmdvUkNnSUlCQklGQ2dOb2FXNFl5SUxScVFZPVwifSIsInZlcnNpb24iOiIxXzAifQ.6x9pj545zFbn9EXHhmrRkfOYK_MkVyQl-kqViBEjuRE',
    'countryCode': 'in',
    'event': {
        'name': 'Skipped Video',
        'eventType': 'native'
    }
}

with open ('Day-6/person.json','w') as json_file:
    json.dump(data,json_file)


with open('Day-6/person.json') as f:
    fileData = json.load(f)

print(json.dumps(fileData, indent=4,sort_keys=True))