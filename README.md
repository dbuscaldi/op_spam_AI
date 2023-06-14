# op_spam_GPT3
AI-generated reviews (GPT-3) mirroring the famous Myle Ott's opinion spam dataset

## Overview
This corpus consists of AI-generated hotel reviews of 20 Chicago hotels.
These reviews were created by feeding to GPT-3 the first 10 words of truthful reviews from the <A HREF="https://myleott.com/op-spam.html">Myle Ott Opinion Spam corpus</A> and asking GPT-3 to complete for a length comparable to the length of the original review.

For the original Myle Ott corpus please download it here: https://myleott.com/op_spam_v1.4.zip

This corpus contains:

- 400 generated positive reviews
- 400 generated negative reviews

Each of the above datasets consist of 20 reviews for each of the 20 most popular Chicago hotels.
The files are named according to the following conventions:

Files are named according to the format used in the Myle Ott corpus: %c_%h_%i.txt, where:

%c denotes the class: (t)ruthful, (d)eceptive or (g)enerated (in our case all are g)

%h denotes the hotel:

- affinia: Affinia Chicago (now MileNorth, A Chicago Hotel)
- allegro: Hotel Allegro Chicago - a Kimpton Hotel
- amalfi: Amalfi Hotel Chicago
- ambassador: Ambassador East Hotel (now PUBLIC Chicago)
- conrad: Conrad Chicago
- fairmont: Fairmont Chicago Millennium Park
- hardrock: Hard Rock Hotel Chicago
- hilton: Hilton Chicago
- homewood: Homewood Suites by Hilton Chicago Downtown
- hyatt: Hyatt Regency Chicago
- intercontinental: InterContinental Chicago
- james: James Chicago
- knickerbocker: Millennium Knickerbocker Hotel Chicago
- monaco: Hotel Monaco Chicago - a Kimpton Hotel
- omni: Omni Chicago Hotel
- palmer: The Palmer House Hilton
- sheraton: Sheraton Chicago Hotel and Towers
- sofitel: Sofitel Chicago Water Tower
- swissotel: Swissotel Chicago
- talbott: The Talbott Hotel

%i serves as a counter to make the filename unique

## References

[1] M. Ott, Y. Choi, C. Cardie, and J.T. Hancock. 2011. Finding Deceptive Opinion Spam by Any Stretch of the Imagination. In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies.

[2] M. Ott, C. Cardie, and J.T. Hancock. 2013. Negative Deceptive Opinion Spam. In Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.
