Socket Programming – Error Detection in Data Transmission
Overview

This project demonstrates data transmission with error detection and correction techniques using socket programming.
It simulates a communication system with a sender, an intermediate server that corrupts data, and a receiver that detects errors.

System Components
Client 1 – Sender

Takes text input from the user

Generates control information using:

Parity Bit

2D Parity

CRC (CRC-8 / CRC-16 / CRC-32)

Hamming Code

Internet Checksum

Sends data in the format:

DATA|METHOD|CONTROL_INFORMATION

Server – Error Injector

Receives packet from Client 1

Injects errors such as:

Bit flip

Character substitution, deletion, insertion

Character swapping

Burst errors

Forwards corrupted data to Client 2 without changing packet structure

Client 2 – Receiver

Recomputes control information based on the method

Compares it with received control data

Displays whether the data is CORRECT or CORRUPTED

Technologies

Python

TCP Socket Programming

Error Detection & Correction Algorithms

How to Run

Start the server

Run Client 2 (receiver)

Run Client 1 (sender)

Purpose

This project was developed for a Computer Networks / Data Communication course to demonstrate practical error detection methods.
