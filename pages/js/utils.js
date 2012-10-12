/**
 * Copyright (C) 2012 Huayra GNU/Linux
 *
 * Author Miguel Angel Garcia <miguel.garcia@gmail.com>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; version 2
 * of the License
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
 * USA.
 */

/**
 * Exits the container application.
 *
 * @param start_next_time boolean Indicates wether the application should autostart
 * on next users login.
 */
function finalize(start_next_time)
{
	qs = start_next_time ? 'autostart' : 'no_autostart';
	window.location='ui://finalize?'+qs;
}

/**
 * Display a bullet.
 */
function show_bullet(bullet)
{
    document.getElementById("title").innerHTML = bullet.title;
    document.getElementById("content").innerHTML = bullet.content;
    document.getElementById("close").style.display = bullet.can_close ? "block" : "none";
    document.getElementById("close-div").style.display = bullet.can_close ? "block" : "none";
    document.getElementById("prev-bullet").style.display = current_bullet > 0 ? "block" : "none";
    document.getElementById("next-bullet").style.display = current_bullet < bullets.length - 1 ? "block" : "none";
}

/**
 * Global var for the current bullet index.
 */
current_bullet = 0;

/**
 * Shows the bullet current_bullet from the bullets array.
 */
function show_current_bullet()
{
    show_bullet(bullets[current_bullet]);
}

/**
 * Displays the first bullet and initializes the navigation.
 */
function start_bullets()
{
    current_bullet = 0;
    show_current_bullet();
}

/**
 * Displays the next bullet and update the current_bullet index. 
 */
function next_bullet()
{
    current_bullet++;
    if(current_bullet < bullets.length)
    {
        show_current_bullet();
    }
}

/**
 * Displays the previous bullet and update the current_bullet index. 
 */
function prev_bullet()
{
    current_bullet--;
    if(current_bullet >= 0)
    {
        show_current_bullet();
    }
}
