#!/bin/perl -w

use Bio::Seq;

$seq_obj = Bio::Seq->new(-file => "test.fasta", -format => "fasta");

while ( $seq_obj = $seqio_obj->next_seq ) {
    # print the sequence
    print $seq_obj->seq,"\n";
}
