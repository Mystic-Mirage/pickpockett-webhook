from microdot import Microdot, Request

from pickpockett_webhook.targets import get_target

app = Microdot()


@app.route("/<target_name>")
async def hook(request: Request, target_name: str):
    if target := get_target(target_name):
        target.hook(request.args["old"], request.args["new"])
    return ""


app.run(port=9191)
