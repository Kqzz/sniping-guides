# Offset / Delay

delay and offset are two words for the same thing. In this guide I will refer to it as offset. *offset is how early your sniper sends snipe requests, measured in milliseconds*. For example, if you have an offset of 30, your sniper will send snipe requests 30 milliseconds before droptime.

> **⚠** This guide is only meant for socket snipers, which have different timings than non-socket snipers. If you are using a non socket sniper, switch to a socket based one as they are far better.

## "Finding" an offset

The reality is, no offset will be "perfect." You also have to understand that finding an offset will take multiple tries, meaning you cannot set your sights on one name and expect to have an accurate offset.

To start, attempt to snipe a name with an offset of between 0 and 50. Somewhere in between there should be a good start. Record the timestamps (they should include a status code such as 403 and a timestamp).

Next, figure out if your snipe requests were early or late by comparing the timestamps to the droptime of the username you attempted to snipe. If you were early, then lower your delay by the number of ms you were early plus 10 (*if that's too complicated, just try lowering by ~20*). If your timestamps were between .01 and .05 after the droptime, then that's a good offset, meaning you should continue sniping with it. If your requests were later than that, raise your offset by how late you were (*again, if that's too complicated, just try raising by ~20*).

Repeat this process until you have an offset that makes your response timestamps be between .01 and .05 after the droptime.

> **If this guide was too complicated, try re-reading it or asking for clarification on a certain section**