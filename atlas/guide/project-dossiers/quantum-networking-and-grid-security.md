# Quantum networking and grid security

## Plain-language summary

ORNL is not only studying quantum computers. It is also testing whether quantum signals can travel through the same kinds of fiber networks used by utilities. The practical question is whether a power grid can use new security methods without losing reliability.

## What the public record shows

In a 2025 test with Chattanooga utility EPB and the University of Tennessee at Chattanooga, ORNL transmitted an entangled quantum signal over multiple wavelength channels. The team used automatic polarization compensation to keep the signal stable as temperature and other conditions changed. The test ran for more than 30 hours with no interruption. [S21]

An earlier ORNL, Los Alamos, EPB, and Qubitekk demonstration tested quantum key distribution across multiple systems connected through substations. The public account says the systems had different hardware and software, so interoperability was part of the test. [S22]

## People and organizations named publicly

- Joseph Chapman, ORNL quantum research scientist and lead for the 2025 study. [S21]
- Muneer Alshowkan, ORNL quantum research scientist who developed the entangled-photon source used at the UTC node. [S21]
- EPB, a Chattanooga utility and telecommunications provider. [S21][S22]
- University of Tennessee at Chattanooga and Qubitekk. [S21][S22]

## Facilities and data

The public evidence identifies commercial fiber, network nodes, substations, reference laser signals, and quantum-photon sources. It does not publish the complete network design, security configuration, keys, operational access, or utility control systems.

## Why it connects to the atlas

This work connects quantum science to grid operations, telecommunications, reliability, and cybersecurity. The unusual part is the testing environment: a real community utility network, not only a laboratory bench.

## Unknowns

- The public sources do not establish production deployment across the U.S. grid.
- They do not establish that quantum networking replaces ordinary utility cybersecurity.
- They do not disclose internal configurations or operational credentials.

## Safe study path

Use a local simulation with three synthetic utility nodes. Model key exchange, link loss, delay, and recovery. Log every event and compare ordinary encryption with a toy quantum-key-distribution message flow. Do not connect to utility networks or use real keys.
