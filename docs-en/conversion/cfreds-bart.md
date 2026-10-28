# From CFReDS to a virtual machine

This page follows a real forensic image, from the portal where it is published to a virtual machine
ready to boot. The image is the "Bart" dataset: a Windows 11 Pro computer, with local and cloud
applications, published on NIST's CFReDS.

```{video} 03-bart-cfreds-conversao
```

## Finding the image

On the [CFReDS](https://cfreds.nist.gov/) portal, search for *ForensicVM*. The dataset describes the
challenge: get into Bart's account without changing the original password and collect local and cloud
evidence. The page points to the files, hosted on Zenodo.

```{figure} /_static/img/03-bart-cfreds-conversao/02a.jpg
:alt: Searching NIST's CFReDS portal

Searching the CFReDS portal.
```

```{figure} /_static/img/03-bart-cfreds-conversao/02b.jpg
:alt: Bart dataset page with the challenge description and the download links

The dataset page, with the challenge description and the links to the files.
```

## Downloading

On Zenodo, the image is split into **ten E01 segments**, 14.9 GB in total. Each segment has its MD5
published. All the segments are downloaded to a folder on the server (the browser transfers a few at a
time).

```{figure} /_static/img/03-bart-cfreds-conversao/03a.jpg
:alt: Zenodo page with the image segments

The files on Zenodo.
```

```{figure} /_static/img/03-bart-cfreds-conversao/03b.jpg
:alt: Zenodo file list with the E01 segments and their download buttons

Downloading the segments one by one (sped up in the video).
```

## Checking integrity

Before converting, confirm that the files arrived intact:

1. Compute the MD5 of each segment on the server and compare it with the one published on Zenodo. In the
   demonstration, all eleven files matched (ten segments plus the instructions).
2. The acquisition *hash* is stored inside the E01 itself. ForensicVM reads it during the conversion and
   records it in the image identity.

```bash
md5sum /path/to/the/segments/*.E??
```

```{tip}
This step is good forensic practice for any transfer of evidence. Always confirm the *hash* before
working with an image and keep the result with the case documentation.
```

## Converting

1. Under **Convert**, choose the **case** (mandatory) and the **equipment** the machine will belong to
   (here, Bart's computer).
2. As the image is already on the server, the source is **Server Path**. Browse to the folder and choose
   the **first segment** (`.E01`). ForensicVM finds the others by itself.
3. Choose the **mode**:
   - **Snapshot:** boots quickly and takes up almost no disk space. The original image is read, but never
     written.
   - **Copy:** takes longer, but the machine becomes independent of the source.
4. Start the conversion.

```{figure} /_static/img/03-bart-cfreds-conversao/05a.jpg
:alt: Conversion wizard with the case, the equipment, the image path and snapshot mode

The conversion wizard: case, equipment, source and mode.
```

## What happens during the conversion

The conversion starts by reading the E01 metadata: the examiner, the acquisition date, the tool used and
the original MD5 and SHA1 *hashes*. It then mounts the image, read-only, and creates the {term}`golden
snapshot`, before any change.

Next, it recognises Windows and injects the VirtIO drivers into a layer of their own, on top of the
image. The page {doc}`driver-injection` explains this step in detail.

```{figure} /_static/img/03-bart-cfreds-conversao/05b.jpg
:alt: Conversion in progress with the image identity and the log of each step

The image identity and the conversion log, live.
```

In the demonstration, converting an 80 GB disk took about eleven minutes. The machine appears in the
case, ready to boot.

## In short

- A public reference image (NIST CFReDS), downloaded and verified by MD5.
- Conversion from a path on the server, with mandatory case and equipment.
- In snapshot mode, the original image is never written.

Next step: {doc}`driver-injection` and then {doc}`../virtual-machines/boot-and-console`.
