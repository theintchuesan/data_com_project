# 📡 Socket Programming – Error Detection Project

## Overview

This project demonstrates data transmission with error detection and correction using Python socket programming.

It consists of three components:
**Client 1 (Sender)**, **Server (Error Injector)**, and **Client 2 (Receiver)**.

## How It Works

* Client 1 sends text data with control information
* Supported methods: **Parity, 2D Parity, CRC, Hamming Code, Internet Checksum**
* Packet format:

  ```
  DATA | METHOD | CONTROL_INFORMATION
  ```
* The server intentionally corrupts the data
* Client 2 verifies the data and reports its integrity

---

## Output

* DATA CORRECT
* DATA CORRUPTED
  

## Purpose
This project is implemented using Python socket programming and was developed for an academic Computer Networks / Data Communication course.
