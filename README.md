# Thue-Morse Sequence
Inspired by Matt Parker's [video](https://www.youtube.com/watch?v=prh72BLNjIk) on fair sharing, I decided to play with the concept some more and generate the sequence as well as to get familiar with matplotlib and numpy.

![alt text](https://raw.githubusercontent.com/lee-pham/Thue-Morse-sequence/master/Traditional.png "Traditional Sequence")
![alt text](https://github.com/lee-pham/Thue-Morse-sequence/blob/master/Thue-Morse.png "Thue-Morse Sequence")

Flashback to recess time during elementary school. It's time for the two team captains to each select 9 other players from a pool of 18 to begin a friendly dodgeball game. Rock-paper-scissors for who picks first and you get seleted second. No biggie right? Your friend/captain got the second best person while the opponent is relegated to the third best. Come game time you can't help but feel a strange feeling in the back of your mind. Overall, the opponent team is better.

That's because if captain A gets to pick 

```[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]``` 

then captain B is forced to choose

```[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]```

The average rank of team A is 100 while the average rank of team B is 110. Captain A consistently gets to pick the better of two players every round.

Using the Thue-Morse sequence, a 'fairer' outcome is possible by alternating captain A and B's turn order. This changes the skillgap of the teams from 1 to 0.2.
