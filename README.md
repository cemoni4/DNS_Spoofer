# 🧬 DNS Spoofer -

This is a Python script for **DNS spoofing**, using `netfilterqueue` and `scapy`.
⚠️ **For educational and CTF testing environments only. Do not use on real networks without permission.**

---

## 🚀 Features

* Intercepts outgoing DNS packets
* Spoofs responses for the domain `cisco.com` 🔁
* Sends a forged DNS response pointing to `140.82.121.4` (GitHub)

---

## 🛠️ Requirements

* Python 3
* Root privileges 🧑‍💻
* Install dependencies:

  ```bash
  pip install netfilterqueue scapy
  ```

---

## 🔧 iptables Configuration

Use the `queses.txt` file for setting up your `iptables` rules.
Basic configuration for local testing:

```bash
sudo iptables --flush
sudo iptables -I INPUT -j NFQUEUE --queue-num 0
sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0
```

For MITM mode:

```bash
sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
```

---

## ▶️ Run the Script

```bash
sudo python3 dns.py
```

---

## 📸 Sample Output

```text
###[ DNS Resource Record ]###
  rrname   = 'cisco.com.'
  type     = A
  rclass   = IN
  ttl      = 10
  rdata    = 140.82.121.4
```

---

## 🛡️ Disclaimer

🔒 This script is **for educational use only**.
🏫 Use **only in controlled environments or CTFs** with explicit authorization.

---

## 📜 License
Distributed under the MIT License.
