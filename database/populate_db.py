# from pinecone_setup import Memory

# mem = Memory()

# Okay, creating a scraper for this is technically possible (not that difficult as well, I can possibly use my own pyba for this!)
# But I am going to hard code this for now. I don't want to waste time on debugging the scraper too.
# I had kept all these answers short and crisp because its going to be SAID out loud. It might come back and bite me though.


# mem.save_faq(
#     question="How do I check my transfer’s status?",
#     answer="""
# The easiest way to check the status of your transfer is by using the tracker in your Wise account:
# - Log in to your Wise account
# - Go to Home to see your activity list
# - Click on the transfer you want to track
# """,
#     section="Transfer status",
#     source="wise",
#     url="https://wise.com/help/articles/2452305/how-do-i-check-my-transfers-status",
# )

# mem.save_faq(
#     question="Where does my money go during the transfer?",
#     answer="""
# Once you send us the money, your transfer goes through a few stages. You'll see these statuses in the tracker:

# - Your money's being processed: This means we're still waiting to receive the money from your bank.
# - Money received: This means we've got your money and we're converting it to the new currency.
# - Transfer Sent: We’ve now sent the money to your recipient’s bank. From here, their bank will process and deliver the money. This can take a few working days. Check your currency for how long it can take.
# - Your money is on its way, but the tracker might not update again until it has been delivered to your recipient's account.
# """,
#     section="Transfer status",
#     source="wise",
#     url="https://wise.com/help/articles/2452305/how-do-i-check-my-transfers-status",
# )

# mem.save_faq(
#     question="Why is my transfer taking longer than expected?",
#     answer="""
# Here are the most common reasons for a delay.
# - It's taking a long time for your money to reach us
# If your transfer has been on Your money's being processed for more than 2 working days, you should check with your bank to make sure they've sent the money to us.
# - We may need to verify your information
# Sometimes we need extra information to meet regulations. If we do, we’ll send you an email explaining what we need. Keep an eye on your inbox so you can provide it quickly.
# - There might be a mistake in the recipient's details
# If there’s a mistake in the recipient’s details, one of two things might happen:
# - Some banks may still process the payment, but it will take them longer.
# - The bank might reject the payment and send it back to us.
# - It’s a weekend or a public holiday
# Banks don’t process transfers during weekends or public holidays. They’ll resume the next working day.

# """,
#     section="Transfer status",
#     source="wise",
#     url="https://wise.com/help/articles/2452305/how-do-i-check-my-transfers-status",
# )

# mem.save_faq(
#     question="How can I speed up my transfer?",
#     answer="""
# If your transfer has been sent but hasn't arrived yet, the quickest way to find it is to give your recipient a transfer receipt. This is a PDF document with all the payment details that their bank can use to track the money.
# """,
#     section="Transfer status",
#     source="wise",
#     url="https://wise.com/help/articles/2452305/how-do-i-check-my-transfers-status",
# )

# # PART 2

# mem.save_faq(
#     question="When will my money arrive after I make a Wise transfer?",
#     answer="""
# When you make a transfer with Wise, you’re given an estimated arrival time. In most cases, your money arrives by that estimate. Delays can still happen depending on bank processing times, recipient details, weekends, or holidays.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# mem.save_faq(
#     question="Wise says my transfer is due to arrive today. What does that mean?",
#     answer="""
# If Wise says your transfer is due today, it usually means the money has already been sent. Some banks take a few extra hours to process incoming transfers, so the money may appear later in the day rather than immediately.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# mem.save_faq(
#     question="Will small typos in the recipient’s name delay my transfer?",
#     answer="""
# Small spelling mistakes in the recipient’s name usually don’t cause issues in most countries. However, for certain currencies such as JPY, name mismatches can cause delays or problems with the transfer.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# mem.save_faq(
#     question="What happens if the recipient’s bank details are wrong?",
#     answer="""
# If key details like the account number are incorrect, the transfer may be delayed or returned to Wise. If the money is returned, Wise will notify you as soon as it happens.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# mem.save_faq(
#     question="Do weekends and holidays affect Wise transfer arrival times?",
#     answer="""
# Yes. Not all banking systems operate on weekends or public holidays. Wise’s delivery estimates account for standard banking hours in the destination country, but local bank schedules can still affect arrival times.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# mem.save_faq(
#     question="Why might a transfer due on Friday arrive later than expected?",
#     answer="""
# Some banks stop processing transfers earlier on Fridays. If your transfer is due on a Friday, it may not appear in the recipient’s account until the next working day.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# mem.save_faq(
#     question="What should I do if my recipient says they haven’t received the money?",
#     answer="""
# Ask your recipient to check their bank statement for a transaction from Wise or one of Wise’s partners. The sender name may not be yours, but the amount and reference can help identify the transfer.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# mem.save_faq(
#     question="Could incorrect recipient bank details cause delays or returns?",
#     answer="""
# Yes. If the recipient’s bank details are incorrect, the transfer may take longer to arrive or be returned to Wise instead of being credited to the recipient’s account.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )


# mem.save_faq(
#     question="What if the recipient’s account is in a different currency?",
#     answer="""
# If the recipient’s account is in a different currency than the one you sent, their bank may convert the money. This can result in the recipient receiving a different amount than what you sent.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )
# mem.save_faq(
#     question="Why might a recipient’s bank say the money hasn’t been credited yet?",
#     answer="""
# The recipient’s bank may already have the money but hasn’t finished processing it into the recipient’s account. In such cases, the transfer exists within the bank’s system but isn’t visible to the recipient yet.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# mem.save_faq(
#     question="How can a receipt help track a delayed Wise transfer?",
#     answer="""
# The Wise receipt includes bank details and, for some currencies, tracking numbers. When shared with the recipient’s bank, it provides all the information needed to locate and trace the transfer.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# mem.save_faq(
#     question="How do I get a PDF receipt for my Wise transfer?",
#     answer="""
# Log into your Wise account, open the transfer, and click the three-dot menu in your browser to download a PDF receipt, or use the receipt button in the app. You can then save and share it with your recipient.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# mem.save_faq(
#     question="Do Wise Interest or Stocks transfers have extra delays?",
#     answer="""
# Yes. Transfers made using Wise Interest or Stocks are subject to daily thresholds. If you exceed those limits, additional delays may apply depending on the asset type.
# """,
#     section="Money withdrawal",
#     source="wise",
#     url="https://wise.com/help/articles/2941900/when-will-my-money-arrive",
# )

# # Part 3, this is also transfer status techincally
# mem.save_faq(
#     question="Why does Wise mark my transfer as complete if the money hasn’t arrived yet?",
#     answer="""
# Wise marks a transfer as Complete once the money has been sent to the recipient’s bank. The arrival estimate already includes extra time for the receiving bank to process and release the funds to the recipient’s account.
# """,
#     section="Transfer status",
#     source="wise",
#     url="https://wise.com/help/articles/2977950/why-does-it-say-my-transfers-complete-when-the-money-hasnt-arrived-yet",
# )

# mem.save_faq(
#     question="Can a transfer be complete while the receiving bank is still processing it?",
#     answer="""
# Yes. Some receiving banks take longer to process incoming transfers and may take up to one working day to release the money. During this time, the funds are with the bank but not yet visible in the recipient’s account.
# """,
#     section="Transfer status",
#     source="wise",
#     url="https://wise.com/help/articles/2977950/why-does-it-say-my-transfers-complete-when-the-money-hasnt-arrived-yet",
# )

# mem.save_faq(
#     question="What can the recipient do if their bank is still processing the transfer?",
#     answer="""
# The recipient can contact their bank and ask them to speed up the processing. They will need a Wise transfer receipt, which contains all the required transaction details.
# """,
#     section="Transfer status",
#     source="wise",
#     url="https://wise.com/help/articles/2977950/why-does-it-say-my-transfers-complete-when-the-money-hasnt-arrived-yet",
# )
# mem.save_faq(
#     question="Could the money have arrived but look different in the recipient’s account?",
#     answer="""
# Yes. The transfer may already be in the recipient’s account but not immediately recognisable. Differences in sender name, reference, currency, or amount can make it harder to identify.
# """,
#     section="Transfer status",
#     source="wise",
#     url="https://wise.com/help/articles/2977950/why-does-it-say-my-transfers-complete-when-the-money-hasnt-arrived-yet",
# )

# mem.save_faq(
#     question="What sender name should the recipient look for on their bank statement?",
#     answer="""
# The recipient should look for a transaction from Wise, not the original sender’s name. In some cases, the transfer may come from one of Wise’s banking partners and can be identified using the reference number.
# """,
#     section="Transfer status",
#     source="wise",
#     url="https://wise.com/help/articles/2977950/why-does-it-say-my-transfers-complete-when-the-money-hasnt-arrived-yet",
# )

# mem.save_faq(
#     question="Why might the received amount be different from what was sent?",
#     answer="""
# If the recipient’s account is in a different currency, their bank may convert the funds again. This additional conversion can result in a different final amount than expected.
# """,
#     section="Transfer status",
#     source="wise",
#     url="https://wise.com/help/articles/2977950/why-does-it-say-my-transfers-complete-when-the-money-hasnt-arrived-yet",
# )

# # part 4

# mem.save_faq(
#     question="Why is my Wise transfer taking longer than the estimated delivery time?",
#     answer="""
# Wise provides an estimated delivery time when you set up a transfer, but delays can occur at different stages of the process. These include delays while your money is reaching Wise, during processing and conversion, or while the recipient’s bank is handling the payment.
# """,
#     section="Transfer delays",
#     source="wise",
#     url="https://wise.com/help/articles/2977951/why-is-my-transfer-taking-longer-than-the-estimate",
# )

# mem.save_faq(
#     question="What does it mean when my money is on its way to Wise?",
#     answer="""
# This means Wise is waiting for your bank to send the money. The speed depends on your bank and the payment method used, and Wise cannot process the transfer until the funds arrive.
# """,
#     section="Transfer delays",
#     source="wise",
#     url="https://wise.com/help/articles/2977951/why-is-my-transfer-taking-longer-than-the-estimate",
# )

# mem.save_faq(
#     question="What happens while Wise is processing my transfer?",
#     answer="""
# During processing, Wise has received your money and is converting it. This stage often includes security checks required by financial regulations, which can add some time.
# """,
#     section="Transfer delays",
#     source="wise",
#     url="https://wise.com/help/articles/2977951/why-is-my-transfer-taking-longer-than-the-estimate",
# )

# mem.save_faq(
#     question="Why can delays happen after Wise sends the money to the recipient?",
#     answer="""
# Once Wise sends the money, the recipient’s bank is responsible for processing it. If the transfer is delayed at this stage, the recipient can ask their bank to investigate using the transfer confirmation.
# """,
#     section="Transfer delays",
#     source="wise",
#     url="https://wise.com/help/articles/2977951/why-is-my-transfer-taking-longer-than-the-estimate",
# )

# mem.save_faq(
#     question="Can security checks delay my Wise transfer?",
#     answer="""
# Yes. Wise may run additional security checks to keep your money safe. If more information is required, such as ID or proof of funds, Wise will contact you by email. These checks cannot be sped up.
# """,
#     section="Transfer delays",
#     source="wise",
#     url="https://wise.com/help/articles/2977951/why-is-my-transfer-taking-longer-than-the-estimate",
# )

# mem.save_faq(
#     question="How does the payment method affect transfer speed?",
#     answer="""
# Different payment methods take different amounts of time to reach Wise. Card payments are usually instant, bank transfers take around 1–4 working days, and SWIFT transfers can take 1–6 working days.
# """,
#     section="Transfer delays",
#     source="wise",
#     url="https://wise.com/help/articles/2977951/why-is-my-transfer-taking-longer-than-the-estimate",
# )

# mem.save_faq(
#     question="Do weekends and public holidays cause Wise transfer delays?",
#     answer="""
# Yes. Banks do not process transfers on weekends or public holidays. Wise estimates only count working days, so transfers sent before weekends or holidays may not move until the next working day.
# """,
#     section="Transfer delays",
#     source="wise",
#     url="https://wise.com/help/articles/2977951/why-is-my-transfer-taking-longer-than-the-estimate",
# )

# mem.save_faq(
#     question="Can mistakes in the recipient’s details delay my transfer?",
#     answer="""
# Yes. Errors in the recipient’s name or account number can cause the receiving bank to reject the transfer and send the money back to Wise.
# """,
#     section="Transfer delays",
#     source="wise",
#     url="https://wise.com/help/articles/2977951/why-is-my-transfer-taking-longer-than-the-estimate",
# )

# mem.save_faq(
#     question="What should I do if my transfer is being returned due to incorrect details?",
#     answer="""
# Check your activity list in Wise. If the status shows the money is being returned, you can correct the recipient’s details or cancel the transfer. Refunds may take a few days depending on the currency and payment method.
# """,
#     section="Transfer delays",
#     source="wise",
#     url="https://wise.com/help/articles/2977951/why-is-my-transfer-taking-longer-than-the-estimate",
# )

# # part 5

# mem.save_faq(
#     question="What is a proof of payment?",
#     answer="""
# A proof of payment is a document that shows you’ve sent money from your bank account. This can be a PDF of your bank statement or a screenshot from your online banking.
# """,
#     section="Payment verification",
#     source="wise",
#     url="https://wise.com/help/articles/2932689/what-is-a-proof-of-payment",
# )

# mem.save_faq(
#     question="Why might Wise ask me for a proof of payment?",
#     answer="""
# Wise may ask for a proof of payment if your money hasn’t reached Wise within the expected timeframe, or if Wise needs to verify that the payment came from a bank account in your name.
# """,
#     section="Payment verification",
#     source="wise",
#     url="https://wise.com/help/articles/2932689/what-is-a-proof-of-payment",
# )

# mem.save_faq(
#     question="How will Wise tell me to upload a proof of payment?",
#     answer="""
# If Wise needs a proof of payment, they will send you an email explaining what to upload and how to submit the document.
# """,
#     section="Payment verification",
#     source="wise",
#     url="https://wise.com/help/articles/2932689/what-is-a-proof-of-payment",
# )

# mem.save_faq(
#     question="What information must be visible on a proof of payment?",
#     answer="""
# A valid proof of payment must clearly show your full name and account number, your bank’s name, Wise’s name and account number, the payment date, amount, currency, and the reference used for the transfer.
# """,
#     section="Payment verification",
#     source="wise",
#     url="https://wise.com/help/articles/2932689/what-is-a-proof-of-payment",
# )

# mem.save_faq(
#     question="Can I submit multiple screenshots as proof of payment?",
#     answer="""
# Yes. If all required details don’t fit in one screenshot, you can submit two screenshots. Both must show your bank account number so Wise can confirm they are from the same account.
# """,
#     section="Payment verification",
#     source="wise",
#     url="https://wise.com/help/articles/2932689/what-is-a-proof-of-payment",
# )

# mem.save_faq(
#     question="What types of proof of payment will Wise not accept?",
#     answer="""
# Wise cannot accept text copied into an email or photos of a computer screen. You must upload a high-quality screenshot or a PDF of an official bank statement.
# """,
#     section="Payment verification",
#     source="wise",
#     url="https://wise.com/help/articles/2932689/what-is-a-proof-of-payment",
# )

# mem.save_faq(
#     question="What proof of payment is required for SWIFT transfers?",
#     answer="""
# For SWIFT transfers, Wise requires a pacs.008 document as the proof of payment.
# """,
#     section="Payment verification",
#     source="wise",
#     url="https://wise.com/help/articles/2932689/what-is-a-proof-of-payment",
# )

# mem.save_faq(
#     question="Are there special proof of payment requirements for Australia or New Zealand?",
#     answer="""
# Yes. For payments from Australia or New Zealand, a screenshot of online banking alone isn’t enough. Wise also needs a recent bank statement showing your name, date of issue, and bank details, or a single bank statement that includes all required information.
# """,
#     section="Payment verification",
#     source="wise",
#     url="https://wise.com/help/articles/2932689/what-is-a-proof-of-payment",
# )

# # part 6

# mem.save_faq(
#     question="What is a banking partner reference number?",
#     answer="""
# A banking partner reference number is an additional reference Wise provides for some transfers. Wise sends money through local banking partners in each country, and this number identifies the transfer within the partner bank’s system.
# """,
#     section="Transfer references",
#     source="wise",
#     url="https://wise.com/help/articles/2977938/whats-a-banking-partner-reference-number",
# )

# mem.save_faq(
#     question="How is a banking partner reference number different from a Wise transfer number?",
#     answer="""
# Every Wise transfer has a Wise transfer number used when contacting Wise support. A banking partner reference number is separate and is only provided for some transfers to help track the payment with the recipient’s bank.
# """,
#     section="Transfer references",
#     source="wise",
#     url="https://wise.com/help/articles/2977938/whats-a-banking-partner-reference-number",
# )

# mem.save_faq(
#     question="How should the banking partner reference number be used?",
#     answer="""
# You should share the banking partner reference number with your recipient. If the transfer shows as completed in Wise, the recipient can give this number to their bank to help locate the payment.
# """,
#     section="Transfer references",
#     source="wise",
#     url="https://wise.com/help/articles/2977938/whats-a-banking-partner-reference-number",
# )

# mem.save_faq(
#     question="Who needs the banking partner reference number to track a transfer?",
#     answer="""
# The recipient needs this reference number when contacting their bank. The recipient’s bank uses it to find the transfer within their system.
# """,
#     section="Transfer references",
#     source="wise",
#     url="https://wise.com/help/articles/2977938/whats-a-banking-partner-reference-number",
# )

# mem.save_faq(
#     question="What is a banking partner reference number called in India?",
#     answer="""
# In India, banks often call the banking partner reference number a UTR (Unique Transaction Reference) number or a transaction reference number.
# """,
#     section="Transfer references",
#     source="wise",
#     url="https://wise.com/help/articles/2977938/whats-a-banking-partner-reference-number",
# )


# Test it out
# results = mem.query("My money hasn't arrived yet! What can be the reasons?")

# top = results[0]
# print(top["answer"])
