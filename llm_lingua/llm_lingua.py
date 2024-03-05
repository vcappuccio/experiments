from pprint import pprint

from dotenv import load_dotenv
from llmlingua import PromptCompressor

load_dotenv('.env')

from langchain.retrievers import ContextualCompressionRetriever
from langchain_community.document_compressors import LLMLinguaCompressor

from retrievers.retriever import get_vector_retriever


def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"Document {i + 1}:\n\n" + d.page_content for i, d in enumerate(docs)]
        )
    )


if __name__ == '__main__':
    # print("Please reference the following examples to answer the math question\n\nQuestion: can buy 4 apples 1 for You bought 36 fruits evenly split between and of 1 $ does cost if total bill $\n's think step\nIf were between 3 of then I 363 = 12 of fruitIf 1 orange then oranges50 $If I I $66 $60 the 2 fruit\n of is, and is then 1W=4If we know we bought 12 and 12W 12\n that can the 12 =\n of apple (60/The\n: Sam a dozen with 30 highighter pens each Heanged into3 the separately the. much\n think boxes120 12 = 360Sam then took 5 boxes × 6 highlighters/box = 30 highlighters.\nHe sold these boxes for 5 * $3 = $15\nAfter selling these 5 boxes there were 360 - 30 = 330 highlighters remaining.\nThese form 330 / 3 = 110 groups of three pens.\nHe sold each of these groups for $2 each, so made 110 * 2 = $220 from them.\nIn total, then, he earned $220 + $15 = $235.\nSince his original cost was $120, he earned $235 - $120 = $115 in profit.\nThe answer is 115\n\nQuestion: Josh decides to try flipping a house.  He buys a house for $80,000 and then puts in $50,000 in repairs.  This increased the value of the house by 150%.  How much profit did he make?")
    #
    #
    # print('LLM Lingua')
    #
    retriever = get_vector_retriever()
    instruction = """Use only information provided below without other sources.  If you don't know the answer, say "I don't know"."""
    # question = "What is the population of Houston, TX?"
    question = "What is the population of New York City?"
    docs = retriever.get_relevant_documents(question)[:1]
    raw_context = [doc.page_content for doc in docs]
    context = "\n\n".join(raw_context)
    print(f"""
    {instruction}
    
    {context}
    
    {question}
    """)

    # llm_lingua = PromptCompressor("lgaalves/gpt2-dolly", device_map="cpu")
    llm_lingua = PromptCompressor(model_name="openai-community/gpt2", device_map="cpu")
    ratio = 0.9
    target_token = -1
    compressed_prompt = llm_lingua.compress_prompt(raw_context, instruction, question, float(ratio), float(target_token))
    pprint(compressed_prompt)
    print(compressed_prompt['compressed_prompt'])

    # compressor = LLMLinguaCompressor(model_name="openai-community/gpt2")
    # instruction = "Please reference the following examples to answer the math question"
    # question = "Question: Josh decides to try flipping a house.  He buys a house for $80,000 and then puts in $50,000 in repairs.  This increased the value of the house by 150%.  How much profit did he make?"
    # context = "Question: Angelo and Melanie want to plan how many hours over the next week they should study together for their test next week. They have 2 chapters of their textbook to study and 4 worksheets to memorize. They figure out that they should dedicate 3 hours to each chapter of their textbook and 1.5 hours for each worksheet. If they plan to study no more than 4 hours each day, how many days should they plan to study total over the next week if they take a 10-minute break every hour, include 3 10-minute snack breaks each day, and 30 minutes for lunch each day?\nLet's think step by step\nAngelo and Melanie think they should dedicate 3 hours to each of the 2 chapters, 3 hours x 2 chapters = 6 hours total.\nFor the worksheets they plan to dedicate 1.5 hours for each worksheet, 1.5 hours x 4 worksheets = 6 hours total.\nAngelo and Melanie need to start with planning 12 hours to study, at 4 hours a day, 12 / 4 = 3 days.\nHowever, they need to include time for breaks and lunch. Every hour they want to include a 10-minute break, so 12 total hours x 10 minutes = 120 extra minutes for breaks.\nThey also want to include 3 10-minute snack breaks, 3 x 10 minutes = 30 minutes.\nAnd they want to include 30 minutes for lunch each day, so 120 minutes for breaks + 30 minutes for snack breaks + 30 minutes for lunch = 180 minutes, or 180 / 60 minutes per hour = 3 extra hours.\nSo Angelo and Melanie want to plan 12 hours to study + 3 hours of breaks = 15 hours total.\nThey want to study no more than 4 hours each day, 15 hours / 4 hours each day = 3.75\nThey will need to plan to study 4 days to allow for all the time they need.\nThe answer is 4\n\nQuestion: Mark's basketball team scores 25 2 pointers, 8 3 pointers and 10 free throws.  Their opponents score double the 2 pointers but half the 3 pointers and free throws.  What's the total number of points scored by both teams added together?\nLet's think step by step\nMark's team scores 25 2 pointers, meaning they scored 25*2= 50 points in 2 pointers.\nHis team also scores 6 3 pointers, meaning they scored 8*3= 24 points in 3 pointers\nThey scored 10 free throws, and free throws count as one point so they scored 10*1=10 points in free throws.\nAll together his team scored 50+24+10= 84 points\nMark's opponents scored double his team's number of 2 pointers, meaning they scored 50*2=100 points in 2 pointers.\nHis opponents scored half his team's number of 3 pointers, meaning they scored 24/2= 12 points in 3 pointers.\nThey also scored half Mark's team's points in free throws, meaning they scored 10/2=5 points in free throws.\nAll together Mark's opponents scored 100+12+5=117 points\nThe total score for the game is both team's scores added together, so it is 84+117=201 points\nThe answer is 201\n\nQuestion: Bella has two times as many marbles as frisbees. She also has 20 more frisbees than deck cards. If she buys 2/5 times more of each item, what would be the total number of the items she will have if she currently has 60 marbles?\nLet's think step by step\nWhen Bella buys 2/5 times more marbles, she'll have increased the number of marbles by 2/5*60 = 24\nThe total number of marbles she'll have is 60+24 = 84\nIf Bella currently has 60 marbles, and she has two times as many marbles as frisbees, she has 60/2 = 30 frisbees.\nIf Bella buys 2/5 times more frisbees, she'll have 2/5*30 = 12 more frisbees.\nThe total number of frisbees she'll have will increase to 30+12 = 42\nBella also has 20 more frisbees than deck cards, meaning she has 30-20 = 10 deck cards\nIf she buys 2/5 times more deck cards, she'll have 2/5*10 = 4 more deck cards.\nThe total number of deck cards she'll have is 10+4 = 14\nTogether, Bella will have a total of 14+42+84 = 140 items\nThe answer is 140\n\nQuestion: A group of 4 fruit baskets contains 9 apples, 15 oranges, and 14 bananas in the first three baskets and 2 less of each fruit in the fourth basket. How many fruits are there?\nLet's think step by step\nFor the first three baskets, the number of apples and oranges in one basket is 9+15=24\nIn total, together with bananas, the number of fruits in one basket is 24+14=38 for the first three baskets.\nSince there are three baskets each having 38 fruits, there are 3*38=114 fruits in the first three baskets.\nThe number of apples in the fourth basket is 9-2=7\nThere are also 15-2=13 oranges in the fourth basket\nThe combined number of oranges and apples in the fourth basket is 13+7=20\nThe fourth basket also contains 14-2=12 bananas.\nIn total, the fourth basket has 20+12=32 fruits.\nThe four baskets together have 32+114=146 fruits.\nThe answer is 146\n\nQuestion: You can buy 4 apples or 1 watermelon for the same price. You bought 36 fruits evenly split between oranges, apples and watermelons, and the price of 1 orange is $0.50. How much does 1 apple cost if your total bill was $66?\nLet's think step by step\nIf 36 fruits were evenly split between 3 types of fruits, then I bought 36/3 = 12 units of each fruit\nIf 1 orange costs $0.50 then 12 oranges will cost $0.50 * 12 = $6\nIf my total bill was $66 and I spent $6 on oranges then I spent $66 - $6 = $60 on the other 2 fruit types.\nAssuming the price of watermelon is W, and knowing that you can buy 4 apples for the same price and that the price of one apple is A, then 1W=4A\nIf we know we bought 12 watermelons and 12 apples for $60, then we know that $60 = 12W + 12A\nKnowing that 1W=4A, then we can convert the above to $60 = 12(4A) + 12A\n$60 = 48A + 12A\n$60 = 60A\nThen we know the price of one apple (A) is $60/60= $1\nThe answer is 1\n\nQuestion: Susy goes to a large school with 800 students, while Sarah goes to a smaller school with only 300 students.  At the start of the school year, Susy had 100 social media followers.  She gained 40 new followers in the first week of the school year, half that in the second week, and half of that in the third week.  Sarah only had 50 social media followers at the start of the year, but she gained 90 new followers the first week, a third of that in the second week, and a third of that in the third week.  After three weeks, how many social media followers did the girl with the most total followers have?\nLet's think step by step\nAfter one week, Susy has 100+40 = 140 followers.\nIn the second week, Susy gains 40/2 = 20 new followers.\nIn the third week, Susy gains 20/2 = 10 new followers.\nIn total, Susy finishes the three weeks with 140+20+10 = 170 total followers.\nAfter one week, Sarah has 50+90 = 140 followers.\nAfter the second week, Sarah gains 90/3 = 30 followers.\nAfter the third week, Sarah gains 30/3 = 10 followers.\nSo, Sarah finishes the three weeks with 140+30+10 = 180 total followers.\nThus, Sarah is the girl with the most total followers with a total of 180.\nThe answer is 180\n\nQuestion: Sam bought a dozen boxes, each with 30 highlighter pens inside, for $10 each box. He rearranged five of these boxes into packages of six highlighters each and sold them for $3 per package. He sold the rest of the highlighters separately at the rate of three pens for $2. How much profit did he make in total, in dollars?\nLet's think step by step\nSam bought 12 boxes x $10 = $120 worth of highlighters.\nHe bought 12 * 30 = 360 highlighters in total.\nSam then took 5 boxes × 6 highlighters/box = 30 highlighters.\nHe sold these boxes for 5 * $3 = $15\nAfter selling these 5 boxes there were 360 - 30 = 330 highlighters remaining.\nThese form 330 / 3 = 110 groups of three pens.\nHe sold each of these groups for $2 each, so made 110 * 2 = $220 from them.\nIn total, then, he earned $220 + $15 = $235.\nSince his original cost was $120, he earned $235 - $120 = $115 in profit.\nThe answer is 115\n\nQuestion: In a certain school, 2/3 of the male students like to play basketball, but only 1/5 of the female students like to play basketball. What percent of the population of the school do not like to play basketball if the ratio of the male to female students is 3:2 and there are 1000 students?\nLet's think step by step\nThe students are divided into 3 + 2 = 5 parts where 3 parts are for males and 2 parts are for females.\nEach part represents 1000/5 = 200 students.\nSo, there are 3 x 200 = 600 males.\nAnd there are 2 x 200 = 400 females.\nHence, 600 x 2/3 = 400 males play basketball.\nAnd 400 x 1/5 = 80 females play basketball.\nA total of 400 + 80 = 480 students play basketball.\nTherefore, 1000 - 480 = 520 do not like to play basketball.\nThe percentage of the school that do not like to play basketball is 520/1000 * 100 = 52\nThe answer is 52\n"
    # ratio = 0
    # target_token = 200
    # compressed_prompt = llm_lingua.compress_prompt(context.split("\n\n"), instruction, question, float(ratio), float(target_token))
    # print(f"""
    # {instruction}
    #
    # {context}
    #
    # {question}
    # """)
    # print(compressed_prompt)
    #
    #
    # #
    # #
    # # compressor = LLMLinguaCompressor(model_name="openai-community/gpt2", device_map="cpu")
    # #
    # #
    # #
    # # compression_retriever = ContextualCompressionRetriever(
    # #     base_compressor=compressor, base_retriever=retriever
    # # )
    # #
    # # compressed_docs = compression_retriever.get_relevant_documents(
    # #     "What do the documents say about the population of Houston TX?"
    # # )
    # # pretty_print_docs(compressed_docs)
