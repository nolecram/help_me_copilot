<?php
// Secure counterpart to Vulnerable.php: a parameterized query prevents SQL injection.

// Validate and cast the input to the expected type before using it.
$articleId = filter_input(INPUT_GET, 'article', FILTER_VALIDATE_INT);
if ($articleId === false || $articleId === null) {
    http_response_code(400);
    exit('Invalid article id');
}

$pdo = new PDO(
    'mysql:host=localhost;dbname=blog;charset=utf8mb4',
    $user,
    $password,
    [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]
);

// The value is bound as a parameter, so it is never concatenated into the SQL string.
$stmt = $pdo->prepare('SELECT * FROM articles WHERE articleid = :articleid');
$stmt->execute([':articleid' => $articleId]);
$article = $stmt->fetch(PDO::FETCH_ASSOC);
