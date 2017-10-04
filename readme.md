ivr
===

This software powers the Interactive Voice response for the
National Yee Emergency Hotline. We provide help to those who
desperately need to hear a yee remix.

# Design

This is currently an MVP. We need to add the systems in place to
make sure there's no downtime, because our clients can't tolerate
any downtime in their busy, yee depraved lives.

We'll probably go with a load balance docker swarm, but who knows
where this crazy adventure will tka eus.


# Setup

## Environmental Variables

```bash
export PROXIED_NUM="+1-XXX-XXX-XXXX"  # The number that is dialed on /forward
```

## Software

```bash
$ make install
```

# Running

```bash
$ ./runServer.sh
```
