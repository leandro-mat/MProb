# Richard Isaac, The Pleasures of Probability — Chapter 3 (printed pages 21-30)
# OCR markdown extracted from isaac.json (mistral-ocr), indices 33-42

<!-- ===== JSON index 33 | printed header: None ===== -->

## 3

# Conditional Probability: From Kings to Prisoners

The naked hulk alongside came,  
And the twain were casting dice;  
'The game is done! I've won! I've won!'  
Quoth she, and whistles thrice.

Samuel Taylor Coleridge, *Rime of the Ancient Mariner*

## 3.1 Some probability rules. Conditional Probability

Again let's roll a pair of dice once, and let's consider the probability set-up with our now familiar 36 possible outcomes and the uniform distribution on the resulting sample space. Let $A$ be the event 'rolling a 7'; in Chapter 1 we saw that this event consists of six outcomes each having probability $1/36$, so $P(A) = 6/36 = 1/6$. Let $B$ be the event 'the first (red) die comes up 1.' If we write down all the outcomes in $B$, we find again six outcomes, namely, $(1,1), (1,2), (1,3), (1,4), (1,5), (1,6)$. So $P(B) = 1/6$ too. Now suppose we compute $P(A \cup B)$. By definition $A \cup B$ is the event occurring when either 7 is rolled or a 1 appears on the first die, or both happen. Write down all the outcomes described by this situation and you will find 11 outcomes: the six ways of rolling 7, which includes the outcome $(1,6)$, plus the other five outcomes with 1 in the first position. According to our rules for computing probabilities $P(A \cup B) = 11/36$. How about $P(A \cap B)$? Well, $A \cap B$ is the event occurring when both $A$ and $B$ happen, namely, when the first die

<!-- ===== JSON index 34 | printed header: 22 3. Conditional Probability: From Kings to Prisoners ===== -->

rolls 1 and we also get 7; this can happen in one way, when (1, 6) appears. Therefore $P(A \cap B) = 1/36$. Notice the validity of the following formula:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B).$$

The reason why this formula holds is pretty easy to grasp. In order to calculate the left-hand side we have to add up the probabilities of all the outcomes in the union set. The union set consists of outcomes in $A$ or $B$ or both. On the right-hand side, $P(A)$ adds up for us all the probabilities of outcomes in $A$, and $P(B)$ adds up probabilities of all outcomes in $B$. But $P(A) + P(B)$ adds the probability of any outcome in *both* $A$ and $B$ exactly twice, once because it is in $A$ and once because it is in $B$. So to get these outcomes in both $A$ and $B$ counted exactly once, we must subtract the term $P(A \cap B)$. The formula above is completely general; it holds for all probability spaces and all pairs of events $A$ and $B$. If we have events $A$ and $B$ such that there are no outcomes in both $A$ and $B$, that is, $A \cap B$ is the empty set, then since the empty set has probability 0 the formula simplifies to

$$P(A \cup B) = P(A) + P(B) \quad (\text{if } A \cap B \text{ is empty}).$$

This formula is nice and simple. It says that if the two events have no common outcomes (in this case we say the events are *disjoint*), then the probabilities just add up to get the probability of the union. You can think of the events $A$ and $B$ as two non-overlapping pieces of land and the probabilities as their areas—the union of the two pieces is just the accumulated land with area just the sum of the two areas. If the pieces of land overlap, then the total property has less area than the sum of the individual areas and you have to use the first formula.

Let's go back to the probability space associated with rolling the pair of dice once and now let's suppose the event $A$ is defined by 'rolling a (total of) 6.' The event $A$ consists of the outcomes $(1, 5), (2, 4), (3, 3), (4, 2)$, and $(5, 1)$, so $P(A) = 5/36$. We have already determined that $B$, the event 'rolling 1 with the first die,' has probability $1/6$. But now suppose you are given some new information. Suppose you are told that indeed it is the case that 1 was rolled with the first die. The question now is, *given this additional information, what is the value of $P(A)$?* It is natural to expect new information to alter your ideas of the uncertainties in the experiment, and therefore cause you to reevaluate the probabilities. In the above example, if it is known that 1 was rolled with the first die, the only possible outcomes are $(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)$; we can ignore the other outcomes because they cannot occur based on the given information. We thus have a new sample space, and it is natural to suppose that in this new sample space each outcome is equally likely, since we started with an equally likely distribution. So *given* that 1 was rolled with the first die, the event $A$ now consists of the unique outcome $(1, 5)$ and it seems as though its probability

<!-- ===== JSON index 35 | printed header: 3.2 Does the king have a sister? 23 ===== -->

should be $1/6$. The additional information updated the probability of $A$ from $5/36$ to $1/6$.

In general, if we have a probability space and then new information arrives, it makes sense for us to update the probability space using the information, and therefore the computation of probabilities is updated based on this new information. When this sort of thing occurs, the updated probabilities are called *conditional probabilities* given the new information. Let us now define $P(A/B)$, the conditional probability of any event $A$ given an event $B$, to be

$$P(A/B) = \frac{P(A \cap B)}{P(B)}.$$

This definition has an intuitive appeal. If $B$ is known to occur, then any outcomes in the original sample space not in $B$ cannot occur, so it makes sense to restrict the outcomes in $A$ we are looking at only to those outcomes also in $B$; that is, $P(A/B)$ should be related to $P(A \cap B)$. In fact, we have defined it to be a value proportional to it. Since $P(B/B)$ should equal 1 on intuitive grounds, we see that the proportionality factor $P(B)$ on the right-hand side of the formula gives you the right answer to get a probability. In the above example, $A \cap B$ consists of the unique $(1, 5)$ with probability $1/36$, and $P(B) = 6/36$, so the formula gives us $P(A/B) = (1/36)/(6/36) = 1/6$ as obtained above. The right side of the conditional probability formula always defines a probability distribution as long as $P(B) \neq 0$; we won't define conditional probabilities when the conditioning event has probability 0. Notice that by multiplying both sides of the conditional probability formula by $P(B)$ we obtain another useful version of the formula:

$$P(B) \cdot P(A/B) = P(A \cap B).$$

The updated conditional probability may have the same value as the original probability: if $A$ is “rolling a 7” and $B$ is “the first die comes up 1,” then it is a simple exercise to obtain $P(A/B) = P(A) = 1/6$. In cases such as this where the conditional probability is the same as the original probability, we say that $A$ is *independent* of $B$: intuitively, the added information provided by $B$ did not give any new information about $A$ in the sense that the conditional probability of $A$ is no different from the original probability. This idea of independence is one of the major topics in probability theory. We start talking about it in earnest in Chapter 5.

## 3.2 Does the king have a sister?

Consider the following problem to test our skills with conditional probability (it appears as an exercise in [28]):

The king comes from a family of two children. What is the probability that the other child is his sister?

<!-- ===== JSON index 36 | printed header: 24 3. Conditional Probability: From Kings to Prisoners ===== -->

The sample space for this problem can be considered to be the set $S$ of four pairs $(B, B), (B, G), (G, B), (G, G)$, where $B$ stands for “boy” and $G$ stands for “girl” and the first and second positions in the pair denote first and second born children, respectively. To be able to do the problem some assumptions must be made. Once again, we shall assume each of the four outcomes is equally likely. Let $U$ be the event “one child is a girl” and $V$ be the event “one child is the king.” What we want to calculate here is $P(U/V)$. Using the formula, we have

$$P(U/V) = \frac{P(U \cap V)}{P(V)} = \frac{P(\text{one child is } B \text{ and one is } G)}{P(V)} = \frac{2/4}{3/4} = 2/3.$$

This problem is tricky—a lot of people think the answer should be $1/2$ as in the car and goat problem. If the question had been “what is the probability that a person’s sibling is a sister,” then the answer would be $1/2$. But in the given problem you are sneakily given the information in the wording of the problem that one child, the king, is male, and that information eliminates the outcome $(G, G)$ in the sample space as a possibility. The remaining three outcomes of $S$ become the conditional, or updated, sample space of which two outcomes have a $B$ and a $G$. This problem illustrates once again how careful you have to be when you are interpreting the information a problem is conveying. If there are ambiguities in the wording, different interpretations may lead you to radically different sample spaces and then to different answers.

### 3.3 The prisoner’s dilemma

A good exercise to get you thinking carefully about conditional probability is a problem called *the prisoner’s dilemma* (there is a completely different and famous problem related to game theory that goes under the same name; see, e.g. [4]). One version of this problem goes as follows: Consider three prisoners, $A$, $B$, and $C$. Two of the prisoners are to be released, and the prisoners know this, but not the identities of the two. Prisoner $A$ asks the guard to tell him the identity of one prisoner other than himself who is to be released. The guard refuses and explains himself by saying to prisoner $A$, “your probability of being released is now $2/3$. If I tell you that $B$, say, is to be released, then you would be one of only two prisoners whose fate is unknown and your probability of release would consequently decrease to $1/2$. Since I don’t want to hurt your chances for release I am not going to tell you.” Is the guard correct in his reasoning?

The answer to this problem is not so obvious; it takes some analytical digging to find out why the guard’s statement sounds a little too glib. The guard is thinking of the sample space of all possibilities of two prisoners released. This can be represented by the set of three outcomes

<!-- ===== JSON index 37 | printed header: 3.3 The prisoner's dilemma 25 ===== -->

$\{A, B\}, \{A, C\}, \{B, C\}$, where curly braces are used to indicate unordered pairs, and the outcome represented by a pair is that those two prisoners are released. So far, the guard has constructed a fine sample space. To get a probability space we use a uniform distribution, which means the parole board chose the prisoners to be released at random. (An assumption like this is necessary for many of these problems. Otherwise there is no obvious probability distribution and the problem can't be done until you get some distribution.) Each of the above outcomes is therefore assigned probability $1/3$, and the guard's first statement about the probability of $A$'s release being initially $2/3$ is correct. The trouble begins when the guard seems to be saying

$$P(A \text{ is released/guard says } B \text{ is released}) = 1/2.$$

The first thing to notice is that the conditional probability given above cannot be computed in terms of the given sample space the guard defined: we simply do not have the event 'guard says $B$ is released' to condition by. This suggests the need for a more complex sample space incorporating the guard's statement. Consider the sample space given by the following four outcomes

$$\begin{aligned} O_1 &= \{A, B, \text{ guard says } B \text{ is released}\}, \\ O_2 &= \{A, C, \text{ guard says } C \text{ is released}\}, \\ O_3 &= \{B, C, \text{ guard says } B \text{ is released}\}, \\ O_4 &= \{B, C, \text{ guard says } C \text{ is released}\}. \end{aligned}$$

These give all the possibilities matching the release of two prisoners with a compatible statement by the guard. The event $O_1$ is equivalent to the event that $A$ and $B$ are released (the guard has no choice of statement), so has probability $1/3$, and similarly $P(O_2) = 1/3$. Now matters get really interesting. Since the union of $O_3$ and $O_4$ is the event $\{B, C\}$, this union has probability $1/3$. But without some further information there is no way to determine the individual probabilities of $O_3$ and $O_4$. Usually, one assumes each of these events is equally likely with probability $1/6$; this corresponds to the guard tossing a coin in case both $B$ and $C$ are released to determine which of the two he should identify to $A$ in his statement. However, he could certainly use some other procedure, for instance, always identifying $B$.

First we will take each event with probability $1/6$. In this case

$$\begin{aligned} P(A \text{ is released/guard says } B \text{ is released}) &= \frac{P(O_1)}{P(\text{guard says } B \text{ is released})} = \frac{1/3}{1/3 + 1/6} = 2/3, \end{aligned}$$

proving the conditional probability of release of $A$ the same as the original unconditional probability. (The term $1/3 + 1/6 = 1/2$ in the formula appears because the event 'guard says $B$ is released' is the union of the

<!-- ===== JSON index 38 | printed header: 26 3. Conditional Probability: From Kings to Prisoners ===== -->

events $O_1$ and $O_3$, which are disjoint. To get the probability of the union, add up the individual probabilities in accordance with the second formula of Section 3.1.) The same argument works in case the event is “guard says $C$ is released,” and again we get $2/3$. So we have solved the problem: the guard has not changed the probability of $A$’s release by giving his statement, that is, the event “$A$ is released” is independent of the event “guard says $B$ is released.”

But now consider the case where the guard *always* identifies $B$ in his statement when both $B$ and $C$ are to be released. Then $O_3$ has probability $1/3$ and $O_4$ has probability 0. In this case, the term $1/3 + 1/6$ in the formula above becomes $1/3 + 1/3 = 2/3$, so the conditional probability is $(1/3)/(2/3) = 1/2$ and now the conditional probability is $1/2$, as the guard had said. So the guard *can* change the value of the conditional probability by altering the way in which he determines his statement when he has a choice (when $B$ and $C$ are both released). He could choose to identify $B$ with any probability from 0 to $1/3$, and the conditional probability will then be some number between $1/2$ and 1. Does this really mean the guard has control over $A$’s fate, as he believes, by the way he determines his statement? This goes against our intuition. If this were true, then if the guard simply whispered his statement to himself in private rather than telling $A$, wouldn’t the same argument given above show that in this way too the guard can alter $A$’s fate? The decision on which prisoners to release was, after all, made by a parole board and had nothing to do with the guard’s statement. What this seems to be suggesting to us is that we should start out by *assuming* the independence of the event “$A$ is released” from the guard’s statement. If this is done, then the conditional probability in the formula above is $2/3$ and the only way this can happen is if $O_3$ and $O_4$ each are given probability $1/6$, as was done for the first solution. So the first solution is the one that meshes with the real world as we perceive it. The other solutions, while mathematically correct, don’t correspond to the model we need here. Observe that if we are interested in the *unconditional* probability $P(A$ is released) rather than a conditional probability, then the answer is just $P(O_1) + P(O_2) = 2/3$ regardless of the way the guard chooses to make his statement.

We have just seen that the solution giving independence of the event “$A$ is released” from the guard’s statement is the reasonable one for the prisoner’s dilemma problem. Let’s see how another problem leads to the same mathematical model as the prisoner’s dilemma problem, except that now *any* possible solution turns out to give a reasonable real-world interpretation. We are going to consider a version of the car and goat problem different from the one discussed in Chapter 1. There, you recall, we assumed your choice of door was random and the car was behind door 1. The original statement of the car and goat problem in the newspaper was a little fuzzy; you could interpret the wording in several ways and get several different problems. The most common version of the problem was described in

<!-- ===== JSON index 39 | printed header: 3.4 All about urns 27 ===== -->

Chapter 1. Another version, analyzed by Gillman [13], assumes you always choose door 1 initially, but the car and goats are distributed at random (namely, uniformly) behind the doors. The host opens either door 2 or 3. You then switch doors. The problem is: find the conditional probability that the car is behind door 2, given that the host opens door 3. This will give the conditional probability of winning if you switch. Gillman showed that the answer depends on the conditional probability of the host opening door 3, given that the car is behind door 1. If the events “winning the car” and “opening door 3” are identified with the events “$A$ is released” and “guard says $B$ is released,” respectively, in the prisoner’s dilemma, we find the problems essentially equivalent. The conditional probability of winning the car given that the host opens door 3 varies between $1/2$ and 1, just as the conditional probability of $A$’s release given that the guard says $B$ is released varies depending upon the probability of the guard making his statement. A major difference between the problems, however, is in the mathematical model the real-life situation suggests. In the prisoner’s dilemma, as we have mentioned, we feel at the outset that $A$’s release should be independent of any statement the guard makes, and we then should build our sample space to reflect that fact. In the case of this new version of the car and goat problem, the nature of the events considered now suggests it is reasonable to assume dependence, so we get a sensible model by assuming any one of the possible solutions discarded previously. That means the answer can reasonably be any number between $1/2$ and 1.

## 3.4 All about urns

Suppose we have an urn containing ten balls, six red and four black. The balls are of the same size and have been mixed up well. You now choose a ball at random from the urn and mark down its color. You do not replace the ball and, after making sure the balls are again well mixed, you choose a second ball from the urn and note its color. Define the events

$$A_1 = \{\text{first ball is red}\},\ A_2 = \{\text{second ball is red}\}.$$

We are interested in the probabilities of the events $A_1, A_1 \cap A_2$, and $A_2$.

The probability of $A_1$ is easy to find. The mixing of the balls is a code expression common in such problems to mean “assume a uniform distribution.” So the sample space can be represented by a set with ten outcomes, each one standing for a ball of a certain color with probability .1 of being selected. The event $A_1$ contains six outcomes, so its probability is .6. Now consider the event $A_1 \cap A_2$. Use the conditional probability formula in the form

$$P(A_1 \cap A_2) = P(A_1) \cdot P(A_2/A_1) = 6/10 \cdot 5/9 = 1/3.$$

The conditional probability in the formula equals $5/9$ because the composition of the urn just before the second selection consists of five red balls

<!-- ===== JSON index 40 | printed header: 28 3. Conditional Probability: From Kings to Prisoners ===== -->

and four black ones, and again we use the uniform distribution because the balls are once again well mixed. Finally, let's consider $A_2$. This event does not depend upon what happens in the first selection. But to calculate this probability we must consider all possibilities of what happened at the first selection because they all contribute a little probability “weight” to the event we're interested in. The important fact is

$$A_2 = (A_1 \cap A_2) \cup (A_1^c \cap A_2)$$

which just says that if we got a red ball on the second selection we either had a red ball on the first selection or *not* a red ball (i.e., a black ball) on the first selection. Since the events in parentheses above are disjoint (you can't simultaneously get both a red and black ball on the first selection), the formula in Section 3.1 for probabilities of disjoint unions gives

$$P(A_2) = P(A_1 \cap A_2) + P(A_1^c \cap A_2).$$

The first term of the sum was just calculated above—we got 1/3. We calculate the second term in exactly the same way, using the formula

$$P(A_1^c \cap A_2) = P(A_1^c) \cdot P(A_2/A_1^c) = 4/10 \cdot 6/9 = 4/15.$$

[There are four black balls before the first selection, so the probability of the first selection yielding a black ball is 4/10; then there are nine balls in the urn, six of them red, and the (conditional) probability of the second selection giving a red ball is 6/9.] So $P(A_2) = 1/3 + 4/15 = .6$.

One of the interesting aspects of the urn problem is that we calculate the probability of an intersection of two events in terms of a given conditional probability. That is in contrast to the problems given in the previous sections where we calculated a conditional probability in terms of initially given probabilities of intersections. In the urn problem the naturally occurring probability is a conditional probability: the probability of the second selection depends on what happened on the first selection.

A second interesting fact is that $A_1$ and $A_2$ have the same probability, .6. This is not just a coincidence of the numbers chosen here. If we take $a$ red balls and $b$ black balls, and only assume there are at least two balls in the urn (so two selections are possible), an easy exercise in algebra shows $A_1$ and $A_2$ still have the same probability which, in this general case, is $a/(a+b)$. At first, this phenomenon may seem curious because the second selection takes place later in time than the first selection and this masks an important symmetry. Instead of thinking of choosing the balls in sequence, imagine that we simply choose *once*, reaching in simultaneously with both hands and selecting a ball with each. We can represent the outcome as an ordered pair like $(R, B)$ where the first coordinate is the color of the ball in the left hand and the second coordinate the color of the ball in the right hand. The ball in the left hand could also be identified with a first ball chosen, and the

<!-- ===== JSON index 41 | printed header: 3.5 Exercises for Chapter 3
29 ===== -->

ball in the right hand with a second ball. Now the choice of the ordered pairs leads to a uniform probability space in the same way as the descriptions of selections in Chapter 2. A symmetry is now apparent in this model: any ordered pair with R as the first coordinate corresponds to an ordered pair with R in the second coordinate by interchanging the first and second coordinates. The number of outcomes in the events A₁ and A₂ are therefore the same, and so we should not now find it surprising that they have the same probability. This way of thinking about the problem also shows that we should expect the same phenomenon at the nth selection if there are enough balls in the urn to make n selections, that is, the probability of selecting a red ball at selection n is still a/(a + b). This example also shows you how looking at a problem in a slightly different way may give insights not so easily obtained from another perspective.

The above model of selecting balls without replacement can be altered in various ways. We could, for example, choose a ball from the urn and if it is red replace the ball and place one additional red ball in the urn. If the ball chosen was black, replace the ball and add one additional black ball to the urn. In this model, the total number of balls in the urn is increasing rather than decreasing. This is a particular case of the so-called Pólya urn scheme which provides a crude model of a contagious disease. Each selection of a ball represents sampling an individual in a certain population. The red ball means the person is infected with the disease; the black ball means that she is free of it. Each discovered infection indicates an increase in the probability of finding another infected individual, and each discovered healthy person indicates an increase in probability for finding another healthy person. Using refined versions of this model, the long-term course of the disease can be studied.

### 3.5 Exercises for Chapter 3

1. Let S be the usual probability space for a pair of dice rolled once, using the uniform distribution. Suppose A is the event “first die is odd,” and B the event “second die is even.” In words, describe each of the following events and calculate their probabilities. (a) A ∩ B, (b) (A ∩ B) ∪ (Aᶜ ∩ Bᶜ), (c) Aᶜ, (d) (A ∪ B)ᶜ.

2. Roll a pair of dice once. What is the probability of getting 11? What is the probability of getting 11, given that the sum of the faces is an odd number? What is the probability of getting 11, given that the sum of the faces is an odd number greater than 3?

3. Toss a coin four times. Find the probability of getting at least two heads. Find the probability of getting at least two heads, given that there was at least one head. Find the probability of getting heads on all four tosses, given at least two heads.

<!-- ===== JSON index 42 | printed header: 30 3. Conditional Probability: From Kings to Prisoners ===== -->

4. An urn contains five red balls and five black ones. A ball is chosen at random and then it, as well as another ball of the same color, is returned to the urn. A second ball is then chosen at random. Find the probabilities that (a) the first ball is red and the second is red, (b) the first ball is red and the second black, (c) the second ball is red, and (d) the second ball is black.

5. Let $A, B$, and $C$ be any events such that $A$ and $A \cap B$ have positive probability. Use the conditional probability formula to prove the relation

$$P(A)P(B/A)P(C/A \cap B) = P(A \cap B \cap C).$$