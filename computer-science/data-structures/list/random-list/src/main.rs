use std::collections::HashMap;

fn fibonacci(n: i128, cache: &mut HashMap<i128, i128>) -> i128 {
    if n < 2 {
        return 1;
    }

    let cached = cache.get(&n);
    match cached {
        Some(n) => return *n,
        None => {
            let result: i128 = fibonacci(n - 1, cache) + fibonacci(n - 2, cache);
            cache.insert(n, result);
            return result;
        }
    }
}

fn main() {
    let mut cache: HashMap<i128, i128> = HashMap::new();

    for n in 0..100 {
        println!("{}: {}", n + 1, fibonacci(n, &mut cache));
    }
}
