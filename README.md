# deal or no deal
create ai to play deal or no deal - may also turn into a analysis of how banker creates deals

I think it may be better to take the deal than you'd think, so I want to really figure out what deals are good.

--

So I just finished both the game code and the different versions of players and bankers.

*Player types:*
- `Player`: random choices
- `MedianDeal`: takes the deal if its above the median of the set of what's next
- `Optimization`: takes the deal if it's above the expected value of continuing to play randomly

*Banker types*
- `Banker`: random offer between 5% and 35% of expected value
- `EmulateRealBanker`: random offer between % ranges that increase as the game continues:
    - 0.07500000000000001 0.38999999999999996
    - 0.2 0.5900000000000001
    - 0.3 0.75
    - 0.375 0.87
    - 0.425 0.95
    - 0.45 0.99
    - 0.475 1.03
    - 0.5 1.0699999999999998
    - 0.525 1.1099999999999999

I used `main.py` to run a game, and `analysis.py` to run 100,000 games at a time. I found that the game acts predictably, according to statistics. Especially when running 100,000 times, the better statistical decisions a player made, the more money they'd win **on average**. This is the main point of what I found. 

I initially wanted to make a neural network-style AI to see if it would do anything interesting, like take the deal every time or always swap the cases at the end, but it really isn't applicable here. Especially when running my analysis with 100,000 games, the decisions are truly entirely statistically-based. If a player makes better statistical decisions, they will perform better over the course of 100,000 games. It's really as simple as that. Maybe if you had one chance at being on the show and you were offered \$150,000 with \$1,000,000 on the board, you should take it because that's "good enough". That term doesn't exist for a computer. If that decision doesn't make statistical sense, it won't make it perform better over the thousands of iterations it takes. So any variance from purely statistical thinking isn't gonna be solved by a computer, it is entierely a human decision driven by human motivations. That's why I don't think an AI will perform much better than the statistical "dumb" `Optimization` player I made. 

The only thing left that I may want to explore is the statistical theory that revealing a case does not change the probablility that the \$1,000,000 case is within the set of cases on stage. There are 26 cases total. If I choose one and reject every deal from the banker until I'm left with my case and one other case. The only two values left are \$0.01 and \$1,000,000. The "expected value" is 500,000.005 *technically*. But statistically, I should always switch because there was a $25/26$ chance that the million was left on stage at the start, and there is still a $25/26$ chance that it's on stage even when it's just the 2 cases left. Does that mean the "true expected value" is \$ $25/26*1,000,000 + 1/26*0.01$? It would somewhat make sense statistically, but it's probably not the case. Becuase we can take the same analysis the exact opposite way. Theres a $25/26$ chance that the \$0.01 was left on the stage at the start as well. This statistical problem only works if someone else is purposely revealing cases that they know to not be the million dollar one. It doesn't work when someone is randomly choosing cases to reveal.

*I'd love to be wrong about this paragraph above ^ so if I am, let me know*