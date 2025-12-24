# Setup instructions

Run:

```sh
uv run agent.py dev
```

Make sure you're on the right project! (this means that your `.env.local` should be correct and pointing to the same project where the SIP trunk was setup)

otherwise run:

```sh
uv run agent.py dev --url "" --api-key "" --api-secret ""
```

That is, explicitly specify this.

The current system:

1. `Twilio's` phone number. Origination connection policy to origination URI from `livekit`
2. Livekit SIP trunk with twilio's phone number and other setup following its documentation
3. Dispatch rule to create a new room and dispatch a "specific agent"
4. Locally hosting the "specific agent"

Just give it some time to restart and all if you're running it after a long time.