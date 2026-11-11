from pyscript import document
from pyscript import web


outcheck = document.getElementById("outcheck")

candidates = ["mark rober", "mister beast", "jarona domingo", "ally hall", "maximum occupancy"]

def process(event):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    newmember = fname + ' ' + lname
    redundcheck = newmember.lower() in candidates
    outcheck.removeAttribute("hidden")

    results = [f"You ain't a member, {newmember}!", f"Hi, {newmember}!"]
    document.getElementById("outcheck").innerHTML = results[redundcheck]