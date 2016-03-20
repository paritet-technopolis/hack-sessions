Love Git'n Money? [Donate](https://live.blockcypher.com/btc/address/3H1YSG26mhENqQMG8hSrTNbaBnopWNNiNP) _All proceeds will go to bounties_

# Why Git Money?

Because something's not right in the world. All you need to do is turn on your
television, open your web browser or read a newspaper. The world is bound to the
will of a small few, who make decisions that aim to decide what's best for the
rest of us - and it's not working. So far these decisions have resulted in wars,
bailouts, inflation, and higher taxes. No doubt, there are many other negatives as well.

And this is why a few of us have built Git Money. This is why we've
chosen a different way. But why? Why choose a more difficult path instead of
doing the other things? Why do people try to swim across the English Channel?
Climb Mount Everest? Run towards danger when everyone else is running away? We
choose this mantra and our currency as bitcoin, not because it is easy, but
because it is hard.

We've said it before and we'll say it again - it doesn't matter where you're
from or who you are. We believe in the right to work anywhere on whatever you
want. It doesn't matter your gender, your education, your social or spiritual
beliefs or your skin color.

We are the Bitcoin Legion. Our home is the Earth and we work in the Cloud - you
are welcome to join us.

## What is Git Money?

[Git Money](http://gitmoney.io) was made with a [21 Bitcoin
Computer](https://21.co/buy/) and enables you to work on whatever you want,
regardless of who you are, where you live, or what you believe and get paid in
bitcoin.

## How it works:

### git opportunities

[Browse current bitcoin-payable Issues on GitHub](https://github.com/21hackers/git-money/issues?q=is%3Aissue+is%3Aopen+label%3A%22git+money%22).
All Issues with a payout will contain the green label **git money** along with a
"**Current Payout:**" when viewed. The current payout for resolving in the issue
is denoted in BTC (Bitcoin) and US Dollars. If you have a question about the
Issue, feel free to comment on it and ask! [New to
git?](https://guides.github.com/activities/hello-world/)

### git work

Once you've found an opportunity, you're halfway home (or wherever it is you're
going!). Go ahead and get to work! All you need to do is clone the repo, create
a branch, commit your changes and submit a pull request. In your pull request
message, [make sure to note that it resolves the
issue](https://github.com/blog/1506-closing-issues-via-pull-requests)  and also include your
bitcoin address.

### git money

Once your pull request is merged, you instantly get paid. However you choose to
git money is up to you. Some people look for small issues that add up to larger
sums. Others go straight for the big jobs. Maybe you're middle of the road,
picking and choosing to make extra money on the side. It's completely up to you
how you want to **git money**.

## Interested in running Git Money in your own repository?

### Requirements
- 21 Bitcoin Computer [https://21.co/buy](https://21.co/buy)
- GitHub Repository [https://github.com/](https://github.com/)
- BitGo Express [https://github.com/BitGo/bitgo-express](https://github.com/BitGo/bitgo-express)

### How it works
1. From the command line on a 21 Bitcoin Computer, run `gitmoney ISSUE DESCRIPTION` with the issue title and the description of the issue that you would like to post to GitHub.
2. Assuming that no errors were encountered, your issue should now appear in your GitHub repository.
3. Post links to your issue on the Internet (Reddit, Twitter, other social media).
4. Review pull requests resolving the issue as they come in.
5. Merge the pull request that best resolves the issue to unlock the payout.

### Installation instructions
1. Install the git-money repository on your 21 Bitcoin Computer as you would with any GitHub repository.
2. In the git-money folder that you just installed on your 21 Bitcoin Computer, run `sudo pip3 install --editable .` to install the gitmoney CLI functionality.
3. Procure a GitHub access token from a repo admin account **[here](https://github.com/settings/tokens)**.
4. Procure a BitGo access token **[here](https://www.bitgo.com)**.
5. Procure Twitter access tokens
6. Export your access tokens:
```
export ACCESS_TOKEN=<BITGO_ACCESS_TOKEN>
export GITHUB_TOKEN=<GITHUB_ACCESS_TOKEN>
export TWITTER_CONSUMER_KEY=<TWITTER_CONSUMER_KEY>
export TWITTER_CONSUMER_SECRET=<TWITTER_CONSUMER_SECRET>
export TWITTER_ACCESS_KEY=<TWITTER_ACCESS_KEY>
export TWITTER_ACCESS_SECRET=<TWITTER_ACCESS_SECRET>
```
7. Set your repo path in /config/config.js
8. To fire the git money server enter `gitmoney --init`
9. To set an issue enter `gitmoney --issue 'ISSUE TITLE' --description 'ISSUE DESCRIPTION'`

### Questions? Comments?

Please join [slack.21.co](https://slack.21.co/) or open an issue.
