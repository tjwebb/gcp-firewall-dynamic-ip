# gcp-firewall-dynamic-ip
Auto-update GCP firewall rule for a dynamic source IP

## Quickstart

### 1. Deploy `checkip` function

```sh
gcloud functions deploy checkip --runtime python37 --trigger-http --memory=128MB

availableMemoryMb: 128
entryPoint: checkip
httpsTrigger:
  url: https://us-central1-tjwebb-test-project.cloudfunctions.net/checkip
```

### 2. Run `update_firewall.py`

```sh
gcloud beta auth application-default login
python update_firewall.py REGION PROJECT_ID RULE_ID

Your ip: 70.199.120.85
Replaced 70.199.148.46 with 70.199.120.85 in rule [ test-rule ]
Done.
```

`REGION` is the region in which you deployed your `checkip` function.

## Other Utils

### Search for IP address in firewall rules

```sh
gcloud beta auth application-default login
python find_firewall_ip.py IP_ADDRESS

```
