# Crypto things
## Encryption vs Signing
- Assymetric encryption encrypts the message with the receiver's public key. The receiver decrypts using the receiver's private key.
- Siging encrypts the message with the sender private key. The receiver decrypts using the sender public key.

Excuse me, WTF?

Assymetric encryption goal is confidentiality. Man in the middle cannot see the message because it has to be decrypted with the receiver's private key.

Signing goal is integrity. Only the correct sender with the right private key may send the message.

# Platform Security
## Trusted Platform Module (TPM)
source: https://trustedcomputinggroup.org/resource/trusted-platform-module-tpm-summary/

"TPM is a computer chip that securely stores artifacts used to authenticate the platform (PC/laptop/etc)". The artifacts include passwords, certificates, encryption keys.