from __future__ import absolute_import, unicode_literals
from .models import SequenceModel
from .services import find_seq
from celery import shared_task


@shared_task(bind=True,  autoretry_for=(Exception,), retry_kwargs={'max_retries': 5, 
                                                                   'countdown': 2})
def process_seq(self,seq,entry_id):
    #entry = SequenceModel.objects.get(pk=entry_id)
    try:
        entry = SequenceModel.objects.get(pk=entry_id)
    except Exception as exc:
        # perhaps retry
        entry = SequenceModel()
        print("ERROR, CANT FIND ASSOCIATED ENTRY")
        return

    entry.result = find_seq(seq)
    print(entry.result) 
    entry.save()
    return entry.result 
