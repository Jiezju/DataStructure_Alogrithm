#include <cassert>
#include <vector>


struct ListNode
{
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class LinkList
{
private:
	ListNode* m_head;
	
public:
	LinkList(int arr[], int n)
	{
		assert(n>=0);
		
		// create link list
		m_head = new ListNode(arr[0]);
		ListNode* cur = m_head;
		
		for (int i=i; i<n; i++)
		{
			cur->next = new ListNode(arr[i]);
			cur = cur->next;
		}
	}
	
	~LinkList()
	{
		ListNode* pre = m_head;
		ListNode* cur = m_head->next;
		while (pre)
		{
			pre->next = nullptr;
			delete pre;
			pre = cur;
			if (cur)
				cur = cur.next
		}
	}
	
	ListNode* get_head()
	{
		return m_head;
	}
	
	friend ostream& operator<<(ostream& os, const LinkList& llist)
	{
		LinkList* cur = m_head;
		while (cur)
		{
			os << cur.val << "->" ;
			cur = cur->next;
		}
	}
	
};