---
layout: single
permalink: /machines/probat/
title: "Probat"
excerpt: "Probatone 5/12/25, P Series"
header:
  overlay_image: /assets/images/probat.jpg
  image: /assets/images/probat.jpg
  teaser: /assets/images/probat.jpg
sidebar:
  nav: "machines"
---

<img class="tab-image" src="{{ site.baseurl }}/assets/images/supporter-badge.png" width="150px">


* __Producer:__ [Probat](http://www.probat-shoproaster.com/en/home/){:target="_blank"}, Germany
* __Machines:__ 
  - Probatone Series II 5Kg/12Kg/25Kg with software option
     - small touch display (Wago PLC)
     - 7" touch display (Beckhof PLC)
  - P Series ([Sample Roaster](https://www.probat.com/en/products/shoproaster/produkte/roasters/sample-roaster/), [1kg/5kg/12kg/25kg](https://www.probat.com/en/products/shoproaster/produkte/roasters/p-series-probatino/)) 
* __Connection:__ MODBUS TCP or WebSocckets via the network
* __Features:__ 
  - logging of environmental temperature (ET), bean temperature (BT), air pressure and related rate-of-rise curves
  - control of burner level, drum- and fan speed

  

### Notes

- ET is not available on machines with the small touch screen and an option for the other machines
- pressure sensor, drum- and fan speed control are options for the machines with 7" touchpad
- the 7" setup defines 3 configurations that can be switched via the command key plus a number key.
  * CMD-1: defines only a slider for burner control
  * CMD-2 (default): adds a second slider for drum speed control
  * CMD-3: adds a third slider for fan speed control
- the air pressure LCD & Curve are hidden by default, but can be made visible by ticking the Curve2/LCD2 flags of the first extra device entry (menu `Config` >> `Device`, tab `Extra Devices`)
- you might need to update your Probatones firmware to the lastest version via Probat to enjoy all features
<!--
- version v1.6.1 of Artisan add support for the [Probat Roaster Middleware](https://www.probat.com/en/products/shoproaster/produkte/roasters/probatone-series/){:target="_blank"} and allows to read data from all its supported roasting machines
-->

**Watch out!** Artisan doesn't monitor unsafe temperatures, so you should never leave the roaster alone.
{: .notice--primary}

**Watch out!** On network problems with a Probatone II with Wago PLC and small touch panel: The small touch panel of the Wago based machines has the fixed IP address 192.168.2.1. Thus on networks running on 192.168.2.x usually the routers IP address is 192.168.2.1 and thus clashes with that internal displays address. Solution: choose an address range for your network different too 192.168.2.x as advised in the roasters manual.
{: .notice--primary}