# Evidence and conversion

This section shows how a forensic image gets into ForensicVM and turns into a bootable virtual machine.
The examples use two public images from [CFReDS](https://cfreds.nist.gov/), NIST's repository of
reference forensic images:

- the **Windows 11 "Bart"** dataset, a Windows 11 Pro computer with local applications and cloud
  services;
- the NIST **Hacking Case**, Greg Schardt's laptop, running Windows XP.

Anyone can download these images to reproduce the demonstrations.

## The conversion steps

Whatever the source, the conversion always follows the same steps:

1. **Case and equipment are mandatory:** the virtual machine is tied to the right item of seized
   equipment.
2. **Reading the image identity:** examiner, acquisition date and tool, original MD5 and SHA1 *hashes*
   (read from the E01 metadata).
3. **Read-only mount** and creation of the {term}`golden snapshot`, before any change.
4. **Operating system detection and driver injection** in a {term}`silver snapshot`.
5. **Detection of the required firmware** (UEFI or BIOS).
6. **Machine ready**, tied to the case, with the conversion in the audit log.

```{toctree}
:maxdepth: 1

cfreds-bart
driver-injection
hacking-case
other-sources
```
