use std::io;
use std::io::Write;
use std::thread;
use std::time::Duration;

fn main() {
    loop {
        let mut input = String::new();
        println!("\nEnter the number you want to factorize or type 'q' to quit");
        print!(">> ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();

        if input.trim() == "q" || input.trim() == "quit" || input.trim() == "exit" {
            println!("Bye bye! :3");
            thread::sleep(Duration::from_secs(1));
            break;
        }
        else if input.trim() == "69" {
           println!("[23, 3, 1]\nHehe ;)");
        }
            
        else {
            let mut num = match input.trim().parse::<i64>() {
                Ok(num) => num,
                Err(e) => {
                    println!("Error: {}", e);
                    continue;
                }
            };

            let mut facts: Vec<i64> = Vec::new();

            while num % 2 == 0 {
                facts.push(2);
                num /= 2
            }
            
            for i in (3..=(f64::sqrt(num as f64) as i64)).step_by(2) {
                while num % i == 0 {
                    facts.push(i);
                    num /= i
                }
            }
            
            if num > 2 {
                facts.push(num);
            }
            
            facts.sort_unstable_by(|a, b| b.cmp(a));
            facts.push(1);
            
            println!("{:?}", facts);                              
        }
    }
}
