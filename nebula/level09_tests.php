<?php

function markup($filename, $use_me)
{
	$contents = file_get_contents($filename);

	$contents = preg_replace("/(\[email (.*)\])/", "spam(\"\\2\")", $contents);
	$contents = preg_replace("/\[/", "<", $contents);
	$contents = preg_replace("/\]/", ">", $contents);

	return $contents;
}

echo markup("email", "abc123");
?>
