import requests

token = "MAGCMcDOvV.._irdF64XEJGlgS_sNqYyX1HBMBLZCfkRseBtBViaUbGGvRsmaNj7ekr3cI55RhBNU2YsneX4XSUHKCFjZttuCZDq7Sq2Y6ueDw9ZC4rJpfG9zhDqDsdIKzng3cKTAbxuiHRvTni8YJ5Lvu1hq62wrtrkCVmp0nqhfmkrD1p_imyAsOXG9YearUaO2DbHJPXUTNFhOmHjb1Ru5Xr1eNR3yKZzozuF1xQ0lFmsDUTeXAA.QXWMhNAnkC0fpi4fx5i8HarWN6Ot4T9znz5k9CVIwndMK3lVGieQGZrhdsHjGjhdSwrdCBh9yJ6sLb2oo.R6gd1EaXWVuutqOFGhXojMJFJWoS4HuumdxSyw7U9MrgdgmaDk6CcESutbvdplRqVMk2POOKBfL6ltOOnV6LbQb5e3lvDz68oqFckT02nPRNYvxdkKHhc16T_LY2oSCQf1hzj1cBa0M31IvjXId8W1vnDi3Zkj8kCfH880kCxUJrUE6tF05Km_xkqZcpX7zHelW0p2xofmYdpjH.13EyyWcx_KdvGYv.K0kg.xtDqLHgIZtTOMGel1MK5.SNgVpPX3JgodmhXii5u_fklJXkUkbPtrwpbmBS.XXuXS2wRabzAavsEjOXA_zinJLqdUV5wdK_MMFQ_XktniuRqf2UPbQ_2gxGPzlh_bH3ozVrgunbvGip6NBFzUJc0gihBJ_c72ADTm5kMxWy31ri.tM3KztWObOvqGlpMNYXmC01mgCHpT34oHYIOmSjsm_zXU6r3GSzCchCCJwMAuP5ZgGDt7veE8oQfp8dL2CWVKAnBNgvKrpMj2DQ.QuEdlD5lvuH7HpkDentxDNGrHRehFTsZCjopZFrptzNQbz_qBDtzsFLQiyVqD6b3RBIJgQ6TTZ5_jQzGb_injNTOWzPfKnyRqpmkTJn8ExfAamvJiguHfow7qfZXG9fnZWL0tNKqOh8coe.XlTEm6cXHFr9pKqdAd"
authorization = "Bearer " + token
# uri = "https://fantasysports.yahooapis.com/fantasy/v2/league/390.l.99174/players;player_keys=390.p.100029/stats;type=week;week=1"
# league_keys = "222.l.498135,242.l.54796,257.l.37493,273.l.11763,314.l.72103,331.l.35354,348.l.88412,359.l.62508,371.l.120246,380.l.709344,390.l.99174"
league_keys = "390.l.99174"
uri = "https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=" + league_keys + ";out=transactions"
headers = {'Authorization': authorization}

r = requests.get(uri, headers=headers)
print(r.status_code)
with open("out.xml", "w") as text_file:
    text_file.write(r.text)