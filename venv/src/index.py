from flask import Flask, request

app = Flask(__name__)
def recursive_fibonacci(n):
    # python sucks in recursive programming
    if n == 0 or n == 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def non_recursive_fibonacci(n):
    if n < 0:
            raise ValueError("n must be non-negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    previous, current = 0, 1
    for i in range(2, n + 1):
        next = previous + current
        previous = current
        current = next

    return current

@app.route("/nonrecursive", methods=["POST"])
def non_rec_fibonacci():
    n = request.args.get('n', default=0, type=int)
    return {'result': non_recursive_fibonacci(n)}, 200

@app.route("/recursive", methods=["POST"])
def rec_fibonacci():
    n = request.args.get('n', default=0, type=int)
    return {'result': recursive_fibonacci(n)}, 200

