# Requirements


## Functional Requirements

#### [FR_1] Editable Test Case

Description:  
User can define their own test case with this testing tool.

Rational:  
Mandatory for testing user's deliverables.

#### [FR_2] Automation Support

Description:  
User can run test cases using this testing tool automatically.

Rational:  
Reduce mistake and save time.

#### [RF_3] Executable Verification with Stream

Description:  
User can verify behavior of executable with this testing tool.
And this testing tool performs verification with checking stream such as stdout, stderr and log file.

Rational:  
Verification of whole executable is required after unittest phase.

#### [RF_4] Crash Detection

Description:  
User does not wait forever for test cases execution even if the process under test crashes.
This testing tool detects crash and make test failed.

This testing tool handles following situation as crash.

* The process under test exits suddenly.
* The process under test stops outputting stream.

Rational:  
Ensure automation of testing.


## Non-Functional Requirements

######  [NFR_1] Portability

Be platform-independent.
This testing tool can be run on following platforms.

* Linux
* Windows
* MacOS
