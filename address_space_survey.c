#include <linux/sched.h>
#include <asm/current.h>
#include <asm/pgtable.h>

asmlinkage void address_space_survey(int first, int last, int *result){
	pgd_t *pgd = current->mm->pgd;
	int address;
	for(address = first ; address <= last ; address++){
		result[address] = pgd_present(pgd[address]);
		
		printk("The number of %d pgd's entry's present bit is %d\n", address, resut[address]);		
	}
}
