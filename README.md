
Header Format of CSV file:
API name, API ID, present(0/1), percentage(real), pattern(1),pattern (2),pattern (3)......, pattern(20)

Total number of APIs = 401

Each Malware set of APIs is terminated by a separator line:
#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,

Total number of samples:
422 benign
374 malware
Labeling is based on the order of appearance in the file
The first 422 samples are benign
The last 374 samples are malware
[ ]
! cat readyForML.csv | grep '\#' | wc -l
account_circle
796
[ ]
374+422
account_circle
796
The benign samples by a separtor line

1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,