# Common Pitfalls by Language (v2.0)

## Go
| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `fatal error: all goroutines asleep - deadlock` | Unbuffered channel with no receiver | Add buffer or ensure receiver exists |
| `panic: concurrent map read and write` | Concurrent map access without sync | Use sync.RWMutex or sync.Map |
| `nil pointer dereference` | Returning nil struct pointer | Initialize struct before returning |
| `context deadline exceeded` | Operation took too long | Add timeout to context |
| `connection refused` | Server not listening | Check if server is started before client |
| `cannot use X (type Y) as type Z` | Type mismatch in interface | Explicit type assertion or conversion |
| `import cycle not allowed` | Circular dependency | Extract shared interface to separate package |

## Python
| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `IndentationError` | Mixed tabs/spaces | Configure editor to use spaces only |
| `NameError: name 'x' is not defined` | Variable scope issue | Check variable initialization |
| `TypeError: 'NoneType' object is not iterable` | Returning None instead of empty collection | Return `[]` instead of `None` |
| `UnicodeEncodeError` | Non-ASCII characters in print | Set `PYTHONIOENCODING=utf-8` |
| `ModuleNotFoundError` | Missing pip install | Add to requirements.txt |
| `RecursionError: maximum recursion depth` | No base case or too deep | Add termination condition or use iteration |
| `KeyError` | Missing dict key | Use `dict.get()` with default |

## JavaScript/TypeScript
| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `Cannot read property 'x' of undefined` | Accessing property on null/undefined | Optional chaining (`?.`) |
| `Promise {<pending>}` | Not awaiting async function | Use `await` or `.then()` |
| `CORS error` | Cross-origin request blocked | Configure CORS headers |
| `Maximum call stack size exceeded` | Infinite recursion | Add termination condition |
| `Variable used before declaration` | Temporal dead zone | Move let/const above usage |
| `TypeError: x is not a function` | Variable shadowing or wrong import | Check import paths and naming |
| `Objects are not valid as a React child` | Rendering object directly | Use JSON.stringify or access property |

## Java
| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `NullPointerException` | Calling method on null object | Check null before call or use Optional |
| `ConcurrentModificationException` | Modifying collection while iterating | Use iterator or copy |
| `OutOfMemoryError` | Memory leak or large data | Increase heap or optimize |
| `IllegalStateException` | Method called in wrong state | Check state machine |
| `ClassNotFoundException` | Missing JAR or classpath | Add dependency to pom.xml/build.gradle |
| `NoSuchMethodError` | API version mismatch | Check dependency versions |
| `StackOverflowError` | Deep recursion | Use iteration or increase stack size |

## Rust
| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `borrow checker error` | Mutable/immutable borrow conflict | Restructure ownership |
| `cannot borrow as mutable because it is also borrowed as immutable` | Multiple immutable borrows | Clone or restructure |
| `thread 'main' panicked` | Unwrap on None/Err | Use `?` or match |
| `ownership moved here` | Value moved without clone | Clone or borrow |
| `trait bound not satisfied` | Missing trait implementation | Implement required trait |
| `use of moved value` | Using value after move | Clone before move or borrow |
| `type annotations needed` | Can't infer type | Add explicit type annotation |

## C++
| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `Segmentation fault` | Null pointer dereference | Use smart pointers (unique_ptr/shared_ptr) |
| `double free or corruption` | Deleting already-freed memory | Use RAII, avoid raw new/delete |
| `undefined reference to vtable` | Missing virtual destructor or implementation | Add virtual destructor to base class |
| `error: no matching function` | Wrong argument types or const mismatch | Check function signature and const-correctness |
| `undefined reference to` | Missing linker dependency | Add .cpp file or library to build |
| `use of deleted function` | Copying non-copyable type | Use std::move or pass by reference |
| `stack overflow` | Large stack allocation | Use heap allocation or increase stack size |

## C#
| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `NullReferenceException` | Accessing member on null | Use null-conditional operator `?.` or nullable reference types |
| `InvalidOperationException` | Collection modified during enumeration | Use ToList() before enumeration |
| `StackOverflowException` | Recursion without base case | Add termination condition |
| `ObjectDisposedException` | Using disposed resource | Check disposal state or use `using` |
| `TaskCanceledException` | Operation timed out or cancelled | Handle cancellation token properly |
| `HttpRequestException` | Network or HTTP error | Add retry policy with Polly |

## Kotlin
| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `NullPointerException` | Java interop null or `!!` on nullable | Use safe call `?.` or `let` |
| `ConcurrentModificationException` | Modifying collection while iterating | Use `toList()` or iterator |
| `IllegalStateException` | Lateinit property not initialized | Use `isInitialized` check or lazy |
| `TypeCastException` | Unsafe cast with `as` | Use `as?` (safe cast) |
| `UninitializedPropertyAccessException` | Accessing lateinit before init | Add initialization guard |

## Swift
| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `unexpectedly found nil` | Force-unwrapping nil optional | Use `if let` or `guard let` |
| `index out of range` | Array access beyond bounds | Check `count` before index access |
| `Thread 1: EXC_BAD_ACCESS` | Accessing deallocated memory | Use weak references, avoid unowned |
| `fatal error: unexpectedly found nil while unwrapping` | Implicitly unwrapped optional is nil | Use optional binding |
| `ambiguous use of` | Overloaded function ambiguity | Explicitly specify types |

## Docker / Kubernetes
| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `CrashLoopBackOff` | Container exits immediately | Check startup command and logs |
| `ImagePullBackOff` | Cannot pull image | Check image name, registry auth |
| `OOMKilled` | Container exceeds memory limit | Increase memory limit or fix leak |
| `Connection refused` | Service not ready or wrong port | Check service selector and port mapping |
| `Cannot connect to the Docker daemon` | Docker not running | Start Docker service |
| `permission denied` | Container running as wrong user | Set USER in Dockerfile or securityContext |
| `no space left on device` | Disk full | Clean up images with `docker system prune` |
