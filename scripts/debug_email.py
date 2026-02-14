import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from integrations.standard_email import StandardEmailService
import asyncio

from integrations.llm_wrapper import UnifiedLLM
from agent.nodes import AgentNodes

async def main():
    print("--- Debugging Email Fetch & Classification ---")
    service = StandardEmailService()
    llm = UnifiedLLM()
    nodes = AgentNodes(llm)
    
    print("Connecting to IMAP...")
    try:
        # Get last 5
        emails = await service.get_unread_emails(max_results=5)
        print(f"\nFound {len(emails)} emails.\n")
        
        for email in emails:
            print(f"Checking ID: {email['id']} | Subject: {email['subject']}")
            
            # Prepare state for classification
            state = {
                "email_subject": email['subject'],
                "email_from": email['from'],
                "email_body": email['body']
            }
            
            print("  > Classifying...")
            result_state = await nodes.classify_email(state)
            
            print(f"  > Valid: {result_state.get('is_valid_inquiry')}")
            print(f"  > Score: {result_state.get('confidence_score')}")
            if not result_state.get('is_valid_inquiry'):
                 print(f"  > Reason: {result_state.get('error', 'Rejected by LLM')}")
            print("-" * 40)
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
