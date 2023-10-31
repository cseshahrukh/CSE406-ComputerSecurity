#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <linux/udp.h>
#include <linux/if_ether.h>
#include <linux/inet.h>

unsigned int a=0, b=0, c=0, d=0, e=0; 
static struct nf_hook_ops hook1, hook2; 

// if you get at least three PING from 10.9.0.1 then drop all packets
unsigned int dropPackets(void *priv, struct sk_buff *skb,
                       const struct nf_hook_state *state)
{
   struct iphdr *iph;
   struct udphdr *udph;

   u16  port   = 53;
   char ip[16] = "10.9.0.1";
   u32  ip_addr;

   if (!skb) return NF_ACCEPT;

   iph = ip_hdr(skb);
   // Convert the IPv4 address from dotted decimal to 32-bit binary
   in4_pton(ip, -1, (u8 *)&ip_addr, '\0', NULL);

   char ipa[16]="192.168.60.5"; 
   char ipb[16]="192.168.60.6"; 
   char ipc[16]="192.168.60.7"; 
   char ipd[16]="10.9.0.5"; 
   char ipe[16]="10.9.0.5";
   u32 ip_addra, ip_addrb, ip_addrc, ip_addrd; 

   in4_pton(ipa, -1, (u8 *)&ip_addra, '\0', NULL);
   in4_pton(ipb, -1, (u8 *)&ip_addrb, '\0', NULL);
   in4_pton(ipc, -1, (u8 *)&ip_addrc, '\0', NULL);
   in4_pton(ipd, -1, (u8 *)&ip_addrd, '\0', NULL);


   if (iph->daddr == ip_addr){
      if (iph->saddr==ip_addra)
      {
         a++; 
         if (a>=3)
            return NF_DROP; 
      }
      else if (iph->saddr==ip_addrb)
      {
         b++; 
         if (b>=3)
            return NF_DROP; 
      }
      else if (iph->saddr==ip_addrc)
      {
         c++; 
         if (c>=3)
            return NF_DROP; 
      }
      else if (iph->saddr==ip_addrd)
      {
         d++; 
         if (d>=3)
            return NF_DROP; 
      }

      //printk(KERN_WARNING "*** Dropping %pI4 (UDP), port %d\n", &(iph->daddr), port);
   //return NF_DROP;
   }
   
   return NF_ACCEPT;



}



int registerFilter(void) {
   printk(KERN_INFO "Registering filters.\n");

   

   hook2.hook = dropPackets;
   hook2.hooknum = NF_INET_POST_ROUTING;
   hook2.pf = PF_INET;
   hook2.priority = NF_IP_PRI_FIRST;
   nf_register_net_hook(&init_net, &hook2);

   return 0;
}

void removeFilter(void) {
   printk(KERN_INFO "The filters are being removed.\n");
   //nf_unregister_net_hook(&init_net, &hook1);
   nf_unregister_net_hook(&init_net, &hook2);
}

module_init(registerFilter);
module_exit(removeFilter);

MODULE_LICENSE("GPL");

