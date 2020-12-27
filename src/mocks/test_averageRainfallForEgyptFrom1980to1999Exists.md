## Interaction 2: GET /climateweb/rest/v1/country/annualavg/pr/1980/1999/egy.xml

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
Date: Sun, 27 Dec 2020 14:53:19 GMT
Content-Type: application/xml
Connection: keep-alive
Set-Cookie: AWSALB=yZAlT45h2v56nB03f9cYIHPKJ3AK4Sja2Dx46cl4JwuqexLh+nrfX2g3jF7wF708eKaMYvDNYp+CzBzfNsHP8FQyCiBvFHavw3fgTFkYpB/5p3Lsj1r1qSpkdpB/; Expires=Sun, 03 Jan 2021 14:53:19 GMT; Path=/, AWSALBCORS=yZAlT45h2v56nB03f9cYIHPKJ3AK4Sja2Dx46cl4JwuqexLh+nrfX2g3jF7wF708eKaMYvDNYp+CzBzfNsHP8FQyCiBvFHavw3fgTFkYpB/5p3Lsj1r1qSpkdpB/; Expires=Sun, 03 Jan 2021 14:53:19 GMT; Path=/; SameSite=None; Secure, TS01c35ec3=010f7a2ab009915a269afe80ddfba341587c03785ac37a33473637fa7662c7cf5583c2862826dadd68fd4c5874f888f2c1f762b5ac; Path=/, climatedataapi.cookie=2631971082.33060.0000; path=/; Httponly, climatedataapi_ext.cookie=2543958026.20480.0000; path=/; Httponly, TS0137860d=01359ee9769034c997ed6469f1e2eca47699f7083fa7ae541d0e2218ef50d1a74b9e94afdb5ccd4f0489b6a1dfe4cd9ba0a686a79458c236fd9340aecd45b201fb8483a9b038f18addf3aa633a7333759e52cf454d807312b83d78bc74cc986d3ac3a91cc532ff01ec677385b154a93dbb9ba2567e66a68821d0aeb2853970a49485cf950c; Path=/
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
      <double>86.9453507501108</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>cccma_cgcm3_1</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>88.30762904406757</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>cnrm_cm3</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>106.36732833443784</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>csiro_mk3_5</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>28.62417012292162</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>gfdl_cm2_0</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>45.26438762045865</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>gfdl_cm2_1</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>26.459523922684326</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>ingv_echam4</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>26.899282784094865</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>inmcm3_0</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>46.921809016059456</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>ipsl_cm4</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>21.791464905471624</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>miroc3_2_medres</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>78.83864541954053</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>miub_echo_g</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>75.66823740260838</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>mpi_echam5</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>31.494514729511625</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>mri_cgcm2_3_2a</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>35.64848946636978</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>ukmo_hadcm3</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>56.096262184318924</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
  <domain.web.AnnualGcmDatum>
    <gcm>ukmo_hadgem1</gcm>
    <variable>pr</variable>
    <fromYear>1980</fromYear>
    <toYear>1999</toYear>
    <annualData>
      <double>63.461061116817845</double>
    </annualData>
  </domain.web.AnnualGcmDatum>
</list>
```
