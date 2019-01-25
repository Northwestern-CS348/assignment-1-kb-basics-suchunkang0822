import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """

        if isinstance(fact,Fact) and not (fact in self.facts):
            self.facts.append(fact)
            return
        elif isinstance(fact,Rule) and not (fact in self.rules):
            self.rules.append(fact)
            return
        print("Asserting {!r}".format(fact))

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        if isinstance(fact,Fact):
            list_of_bindings = ListOfBindings()
            for f in self.facts:
                bindings = match(fact.statement,f.statement)
                if bindings:
                    list_of_bindings.add_bindings(bindings,[fact,f])
                    # print("000000000")
                    # print(f.statement)
                    # print(fact.statement)
                    # print(bindings)
                    # # print(list_of_bindings)
            if not len(list_of_bindings.list_of_bindings) == 0:
                return list_of_bindings
            else:
                return False


        print("Asking {!r}".format(fact))

