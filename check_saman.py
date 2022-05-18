from urllib import request
import json

def checkSaman(vehNo):
    url = "http://johor.ekhidmat.my/ekhidmat/compoundchecking/getdata?compoundtype=K"

    body = {
        "accounttype": "4",
        "vehicleNo": vehNo
    }

    print("\nChecking your vehicle number for MBJB compound... " + vehNo + "\n")

    body = json.dumps(body)

    req = request.Request(
        url = url,
        headers = {
            "content-type": "application/json; charset=utf-8",
            "key": "44268aa18250e21ac85c0ec3062932cf",
            "accept": "*/*",
            "origin": "http://johor.ekhidmat.my",
            "referer": "http://johor.ekhidmat.my/ekhidmat/compoundchecking"
        },
        data = bytes(body, "utf-8"),
        method = "POST"
    )

    with request.urlopen(req) as res:    
        if res.status != 200:
            print("Dang it! An error occured.")
        else:
            print("Server is returning something. Hmm... Sus...\n")

            resDatBuf = res.read().decode("utf-8")

            comps = json.loads(resDatBuf)

            if len(comps) == 0:
                print("No compound found.")
            else:
                comp = comps[0]

                s = "s" if comp["count"] > 1 else ""

                print("Congrats! You got " + str(comp["count"]) + " compound" + s + "!")
                print("Total: RM " + str(comp["total"]))
           
print("\nEnter your vehicle number: ")

vehNo = input()

checkSaman(vehNo)