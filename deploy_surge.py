import pexpect
import sys

print("Starting Surge deployment...")
child = pexpect.spawn('bash', ['-c', 'export PATH=/tmp/node-v20.11.1-darwin-arm64/bin:$PATH && surge ./ coolcare-qatar-preview.surge.sh'])
child.logfile = sys.stdout.buffer

try:
    index = child.expect(['email:', 'Login \(or create account\):', pexpect.EOF], timeout=10)
    if index == 0 or index == 1:
        child.sendline('testuser_coolcareqatar99@example.com')
        child.expect('password:', timeout=5)
        child.sendline('Qazwsx123!!')
        
    child.expect(pexpect.EOF, timeout=60)
except Exception as e:
    print("\nError:", e)
