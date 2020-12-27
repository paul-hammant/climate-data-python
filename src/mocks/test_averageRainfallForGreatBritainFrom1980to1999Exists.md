## Interaction 1: GET /climateweb/rest/v1/country/annualavg/pr/1980/1999/gbr.xml

### Request headers recorded for playback:

```
Host: climatedataapi.worldbank.org
User-Agent: Servirtium-Testing
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Date: Sun, 27 Dec 2020 14:53:18 GMT
Content-Type: application/xml
Connection: keep-alive
Set-Cookie: AWSALB=8vNRHKn1Y9bfeBHVlTHmiqhU0/DltgrRPnE2tMtnO/iAulbSyXlNVO+bP4ijqAOBxGzkO2DvaAZNd9LTl/eArsIg44Wn8RH48D72ZWSiLRtGJ2o4gGS84+fUP5eX; Expires=Sun, 03 Jan 2021 14:53:18 GMT; Path=/, AWSALBCORS=8vNRHKn1Y9bfeBHVlTHmiqhU0/DltgrRPnE2tMtnO/iAulbSyXlNVO+bP4ijqAOBxGzkO2DvaAZNd9LTl/eArsIg44Wn8RH48D72ZWSiLRtGJ2o4gGS84+fUP5eX; Expires=Sun, 03 Jan 2021 14:53:18 GMT; Path=/; SameSite=None; Secure, TS01c35ec3=010640bd98675310ddad86770a949643e186baad5710cc5f27662b9686589e2c5bbbe0f79af3b0e48024ba71941ca3c41a0e28678b; Path=/, climatedataapi.cookie=316717322.33060.0000; path=/; Httponly, climatedataapi_ext.cookie=2543958026.20480.0000; path=/; Httponly, TS0137860d=01359ee976e54c6c3d21b4fa7d535e64e361b400b250db53aef80a25e9001547554aaab0abd6efad9b12c824d19b6b462d2c8f7d51db25d418cc3b99bd47206a2a91ec1aa93933927dec7bc2f2bb037bc2f522f6f015695d5d6e2fccb2638bca2255a7e41538b0812cb74fe75aeffba9c2be9ed1925d060763b080c8de3acc3fb9c5350e68; Path=/
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: X-Requested-With
Access-Control-Allow-Methods: GET
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'
X-Frame-Options: deny
Cache-Control: no-cache,no-store
Pragma: no-cache
Secure: true
HttpOnly: true
Transfer-Encoding: chunked
```

### Response body recorded for playback (200: application/xml):

```
<list>
  <domain.web.AnnualGcmDatum>
    <gcm>bccr_bcm2_0</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>987.9504418944</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>cccma_cgcm3_1</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>815.2627636718801</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>cnrm_cm3</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>1099.3898999037601</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>csiro_mk3_5</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>1021.6996069333198</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>gfdl_cm2_0</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>1019.8750146478401</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>gfdl_cm2_1</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>1084.5603759764</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>ingv_echam4</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>1008.2985131833999</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>inmcm3_0</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>1194.9564575200002</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>ipsl_cm4</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>893.9680444336799</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>miroc3_2_medres</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>1032.85460449136</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>miub_echo_g</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>905.9324633786798</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>mpi_echam5</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>1024.2805590819598</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>mri_cgcm2_3_2a</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>784.5488305664002</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>ukmo_hadcm3</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>957.3522631840398</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>ukmo_hadgem1</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>1001.7526196294</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
</list>
```
