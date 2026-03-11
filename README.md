# Symmetric File Encryption using Python

## Project Overview

This project demonstrates **symmetric encryption** using Python.
A secret key is generated and stored in a file. The same key is used to **encrypt and decrypt** a file.

In symmetric encryption, the **same key is used for both encryption and decryption**.

## Files in the Project

### `sample.txt`
The file that will be encrypted and decrypted.

### `keygen.py`
Generates a **secret key** and saves it in `secret.key`.

### `secret.key`
Stores the encryption key used to lock and unlock the file.

### `encrypt.py`
Reads the key from `secret.key` and **encrypts the file**.

### `decrypt.py`
Reads the key from `secret.key` and **decrypts the file**.

## How It Works

1. Run `keygen.py`
2. A secret key is created and saved in `secret.key`
3. Run `encrypt.py` to encrypt `sample.txt`
4. The file becomes unreadable
5. Run `decrypt.py` to restore the original content

## Installation

Install the required library:
pip install cryptography

## Running the Project

Generate key:
python keygen.py

Encrypt file:
python encrypt.py

Decrypt file:
python decrypt.py

## Important Notes

1. Do **not delete `secret.key`**
2. If the key is lost, the encrypted file **cannot be decrypted**
3. This project is for **educational purposes**

## Concept Learned

1. Symmetric encryption
2. File handling in Python
3. Cryptography basics
4. Secure data protection
