
$IPTABLES -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

$IPTABLES -A OUTPUT -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT
$IPTABLES -A OUTPUT -j ACCEPT

$IPTABLES -A FORWARD -j REJECT

$IPTABLES -N REJECTLOG
$IPTABLES -A REJECTLOG -j LOG --log-level debug --log-tcp-sequence --log-tcp-options --log-ip-options -m limit --limit 3/s --limit-burst 8 --log-prefix "REJECT "
$IPTABLES -A REJECTLOG -p tcp -j REJECT --reject-with tcp-reset
$IPTABLES -A REJECTLOG -j REJECT

$IPTABLES -A INPUT -j REJECTLOG